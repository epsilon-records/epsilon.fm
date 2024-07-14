# Built-in Dependencies
from datetime import datetime, timedelta, UTC
from typing import Union, Literal, Dict, Any

# Third-Party Dependencies
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
import bcrypt

# Local Dependencies
from src.apps.auth.schemas import TokenData, TokenBlacklistCreate
from src.apps.auth.crud import crud_token_blacklist
from src.apps.admin.users.crud import crud_users
from src.core.config import settings
from src.core.utils import cache

# Constants for token-related settings
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS = settings.REFRESH_TOKEN_EXPIRE_DAYS

# OAuth2PasswordBearer instance for handling token retrieval from requests
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/system/auth/login")


# Function to verify plain password against hashed password
async def verify_password(plain_password: str, hashed_password: str) -> bool:
    correct_password: bool = bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
    return correct_password


# Function to generate hashed password from plain password
def get_password_hash(password: str) -> str:
    hashed_password: str = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    return hashed_password


# Function to authenticate a user based on provided credentials
async def authenticate_user(
    username_or_email: str, password: str, db: AsyncSession
) -> Union[Dict[str, Any], Literal[False]]:
    if "@" in username_or_email:
        db_user = await crud_users.get(db=db, email=username_or_email, is_deleted=False)
    else:
        db_user = await crud_users.get(db=db, username=username_or_email, is_deleted=False)

    if not db_user:
        return False

    elif not await verify_password(password, db_user["hashed_password"]):
        return False

    return db_user


# Function to create an access token with optional expiration time
async def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC).replace(tzinfo=None) + expires_delta
    else:
        expire = datetime.now(UTC).replace(tzinfo=None) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Function to create a refresh token with optional expiration time
async def create_refresh_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC).replace(tzinfo=None) + expires_delta
    else:
        expire = datetime.now(UTC).replace(tzinfo=None) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Function to verify the validity of a token and return TokenData if valid
async def verify_token(token: str, db: AsyncSession) -> TokenData | None:
    """
    Verify a JWT token and return TokenData if valid.

    Parameters
    ----------
    token: str
        The JWT token to be verified.
    db: AsyncSession
        Database session for performing database operations.

    Returns
    ----------
    TokenData | None
        An instance of TokenData representing the user if the token is valid.
        None is returned if the token is invalid or the user is not active.
    """
    is_blacklisted = await crud_token_blacklist.exists(db, token=token)
    if is_blacklisted:
        return None

    try:
        # Decode the token payload and extract the subject (username or email)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username_or_email: str = payload.get("sub")
        if username_or_email is None:
            return None

        # Check if the Redis client is available
        if cache.client:
            # Check if user is active in Redis
            is_active = await cache.client.hget(
                settings.REDIS_HASH_SYSTEM_AUTH_VALID_USERNAMES,
                username_or_email,
            )

            if is_active:
                return TokenData(username_or_email=username_or_email)

        # If not active in Redis or Redis is not available, check PostgreSQL
        user = await crud_users.get(db=db, username=username_or_email, is_deleted=False)

        if user:
            # Update Redis with user active status if Redis is available
            if cache.client:
                await cache.client.hset(
                    settings.REDIS_HASH_SYSTEM_AUTH_VALID_USERNAMES,
                    username_or_email,
                    "active",
                )

            return TokenData(username_or_email=username_or_email)

        # If user is not found in Redis or PostgreSQL, blacklist the token
        await blacklist_token(token=token, db=db)

        return None

    except JWTError:
        return None


# Function to blacklist a token by storing it in the database
async def blacklist_token(token: str, db: AsyncSession) -> None:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    expires_at = datetime.fromtimestamp(payload.get("exp"))
    await crud_token_blacklist.create(
        db,
        object=TokenBlacklistCreate(**{"token": token, "expires_at": expires_at}),
    )
