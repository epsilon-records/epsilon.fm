# Built-in Dependencies
from typing import Annotated, Union, Any

# Third-Party Dependencies
from fastapi import Depends, HTTPException, Request
from sqlmodel.ext.asyncio.session import AsyncSession

# Local Dependencies
from src.apps.system.rate_limits.crud import crud_rate_limits
from src.apps.system.rate_limits.schemas import sanitize_path
from src.core.utils.rate_limit import is_rate_limited
from src.apps.system.tiers.crud import crud_tiers
from src.apps.admin.users.crud import crud_users
from src.core.exceptions.http_exceptions import (
    UnauthorizedException,
    ForbiddenException,
    RateLimitException,
)

from src.core.db.session import async_get_db
from src.apps.admin.users.models import User
from src.core.security import oauth2_scheme
from src.core.security import verify_token
from src.core.config import settings
from src.core.logger import logging

# Logger instance
logger = logging.getLogger(__name__)

# Default rate limit settings from configuration
DEFAULT_LIMIT = settings.DEFAULT_RATE_LIMIT_LIMIT
DEFAULT_PERIOD = settings.DEFAULT_RATE_LIMIT_PERIOD


# Function to get the current user based on the provided authentication token
async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Union[dict[str, Any], None]:
    token_data = await verify_token(token, db)
    if token_data is None:
        raise UnauthorizedException(detail="User not authenticated.")

    # Check if the authentication token represents an email or username and retrieve the user information
    if "@" in token_data.username_or_email:
        user: dict | None = await crud_users.get(
            db=db, email=token_data.username_or_email, is_active=True, is_deleted=False
        )
    else:
        user = await crud_users.get(
            db=db, username=token_data.username_or_email, is_active=True, is_deleted=False
        )

    if user:
        # Return the user information if available
        return user

    # Raise an exception if the user is not authenticated
    raise UnauthorizedException(detail="User not authenticated.")


# Function to get the optional user based on the provided request
async def get_optional_user(
    request: Request, db: AsyncSession = Depends(async_get_db)
) -> dict | None:
    token = request.headers.get("Authorization")
    if not token:
        return None

    try:
        # Parse the Authorization token and verify it to obtain token data
        token_type, _, token_value = token.partition(" ")
        if token_type.lower() != "bearer" or not token_value:
            # Return None if the token is not a bearer token
            return None

        token_data = await verify_token(token_value, db)
        if token_data is None:
            # Return None if token verification fails
            return None

        # Retrieve the current user information based on the token data
        return await get_current_user(token_value, db=db)

    except HTTPException as http_exc:
        if http_exc.status_code != 401:
            # Log unexpected HTTPException with non-401 status code.
            logger.error(f"Unexpected HTTPException in get_optional_user: {http_exc.detail}")
        return None

    except Exception as exc:
        # Log unexpected errors during execution.
        logger.error(f"Unexpected error in get_optional_user: {exc}")
        return None


# Function to get the current superuser based on the provided current user information
async def get_current_superuser(current_user: Annotated[dict, Depends(get_current_user)]) -> dict:
    if not current_user["is_superuser"]:
        raise ForbiddenException(detail="You do not have enough privileges.")

    return current_user


# Function to apply rate limiting to the incoming request
async def rate_limiter(
    request: Request,
    db: Annotated[AsyncSession, Depends(async_get_db)],
    user: User | None = Depends(get_optional_user),
) -> None:
    # Sanitize the path from the request URL
    path = sanitize_path(request.url.path)
    if user:
        # If a user is present, retrieve user-specific rate limit settings
        user_id = user["id"]
        tier = await crud_tiers.get(db, id=user["tier_id"])
        if tier:
            rate_limit = await crud_rate_limits.get(db=db, tier_id=tier["id"], path=path)
            if rate_limit:
                # If rate limit settings are found, use them; otherwise, apply default settings
                limit, period = rate_limit["limit"], rate_limit["period"]
            else:
                logger.warning(
                    f"User {user_id} with tier '{tier['name']}' has no specific rate limit for path '{path}'. Applying default rate limit."
                )
                limit, period = DEFAULT_LIMIT, DEFAULT_PERIOD
        else:
            logger.warning(f"User {user_id} has no assigned tier. Applying default rate limit.")
            limit, period = DEFAULT_LIMIT, DEFAULT_PERIOD
    else:
        # If no user is present, apply default rate limit settings based on the client host
        if hasattr(request, "client") and hasattr(request.client, "host"):
            # Check this issue comment if you are using Gunicorn:
            # https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/224#issuecomment-1429593840
            user_id = request.client.host
        else:
            x_forwarded_for = request.headers.get("x-forwarded-for", None)
            x_real_ip = request.headers.get("x-real-ip", None)
            user_id = (
                x_forwarded_for if x_forwarded_for else (x_real_ip if x_real_ip else "Unknown")
            )

        limit, period = DEFAULT_LIMIT, DEFAULT_PERIOD

    # Check if the user is rate-limited for the given path
    is_limited = await is_rate_limited(
        app=request.app,
        db=db,
        user_id=user_id,
        path=path,
        limit=limit,
        period=period,
    )
    if is_limited:
        # Raise an exception if the user exceeds the rate limit
        raise RateLimitException(detail="Rate limit exceeded.")
