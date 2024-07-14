# Built-in Dependencies
from typing import Annotated, Dict, Any
from uuid import UUID

# Third-Party Dependencies
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import Depends, Request
import fastapi

# Local Dependencies
from src.core.api.dependencies import get_current_user, get_current_superuser
from src.apps.system.rate_limits.crud import crud_rate_limits
from src.apps.admin.users.crud import crud_users
from src.apps.system.tiers.crud import crud_tiers
from src.apps.system.tiers.schemas import TierRead
from src.apps.system.tiers.models import Tier
from src.core.db.session import async_get_db
from src.core.exceptions.http_exceptions import (
    DuplicateValueException,
    NotFoundException,
    ForbiddenException,
    BadRequestException,
)
from src.apps.admin.users.schemas import (
    User,
    UserCreate,
    UserCreateInternal,
    UserUpdate,
    UserRead,
    UserTierUpdate,
)
from src.core.utils.paginated import (
    PaginatedListResponse,
    paginated_response,
    compute_offset,
)
from src.core.security import get_password_hash, blacklist_token, oauth2_scheme
from src.core.config import settings
from src.core.utils import cache

router = fastapi.APIRouter(tags=["Admin - Users"])


@router.post("/admin/users", response_model=UserRead, status_code=201)
async def write_user(
    request: Request,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    user: UserCreate,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> UserRead:
    email_row = await crud_users.exists(db=db, email=user.email)
    if email_row:
        raise DuplicateValueException(detail="Email is already registered")

    username_row = await crud_users.exists(db=db, username=user.username)
    if username_row:
        raise DuplicateValueException(detail="Username not available")

    user_internal_dict = user.model_dump()
    user_internal_dict["hashed_password"] = get_password_hash(
        password=user_internal_dict["password"]
    )
    del user_internal_dict["password"]

    default_tier = await crud_tiers.get(db=db, schema_to_select=TierRead, default=True)
    if default_tier is None:
        raise BadRequestException(
            detail="No default tier found. Please create a default tier first."
        )

    user_internal_dict["tier_id"] = default_tier["id"]

    user_internal = UserCreateInternal(**user_internal_dict)
    return await crud_users.create(db=db, object=user_internal)


@router.get("/admin/users", response_model=PaginatedListResponse[UserRead])
async def read_users(
    request: Request,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
    page: int = 1,
    items_per_page: int = 10,
) -> dict:
    users_data = await crud_users.get_multi(
        db=db,
        offset=compute_offset(page, items_per_page),
        limit=items_per_page,
        schema_to_select=UserRead,
        is_deleted=False,
    )

    return paginated_response(crud_data=users_data, page=page, items_per_page=items_per_page)


@router.get("/admin/users/me/", response_model=UserRead)
async def read_users_me(
    request: Request,
    current_user: Annotated[UserRead, Depends(get_current_user)],
) -> UserRead:
    return current_user


@router.get("/admin/users/{user_id}", response_model=UserRead)
async def read_user(
    request: Request,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    user_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> dict:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    return db_user


@router.patch("/admin/users/{user_id}")
async def patch_user(
    request: Request,
    values: UserUpdate,
    user_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    # Check if the user is not a superuser and is not updating their own user
    if not current_user["is_superuser"] and str(db_user["id"]) != str(current_user["id"]):
        raise ForbiddenException(detail="You are not allowed to update this user")

    if values.username != db_user["username"]:
        existing_username = await crud_users.exists(db=db, username=values.username)
        if existing_username:
            raise DuplicateValueException(detail="Username not available")

    if values.email != db_user["email"]:
        existing_email = await crud_users.exists(db=db, email=values.email)
        if existing_email:
            raise DuplicateValueException(detail="Email is already registered")

    await crud_users.update(db=db, object=values, id=user_id)
    return {"message": "User updated"}


@router.delete("/admin/users/{user_id}")
async def erase_user(
    request: Request,
    user_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
    token: str = Depends(oauth2_scheme),
) -> Dict[str, str]:
    db_user = await crud_users.get(db=db, schema_to_select=User, id=user_id)
    if db_user is None:
        raise NotFoundException(detail="User not found")
    if db_user["is_deleted"]:
        if current_user["is_superuser"]:
            raise NotFoundException(detail="User already deleted (soft delete).")
        raise NotFoundException(detail="User not found")

    # Check if the user is not a superuser and is not deleting their own user
    if not current_user["is_superuser"] and str(db_user["id"]) != str(current_user["id"]):
        raise ForbiddenException(detail="You are not allowed to delete this user")

    # Soft delete user on the database
    await crud_users.delete(db=db, db_row=db_user, id=user_id)

    # Remove user from Redis cache
    if cache.client:
        await cache.client.hdel(
            settings.REDIS_HASH_SYSTEM_AUTH_VALID_USERNAMES, db_user["username"]
        )

    return {"message": "User deleted"}


@router.delete("/admin/users/{user_id}/db", dependencies=[Depends(get_current_superuser)])
async def erase_db_user(
    request: Request,
    user_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id)
    if not db_user:
        raise NotFoundException(detail="User not found")

    # Delete user from the database
    try:
        await crud_users.db_delete(db=db, id=user_id)
    except IntegrityError:
        raise ForbiddenException(detail="User cannot be deleted")

    # Remove user from Redis cache
    if cache.client:
        await cache.client.hdel(
            settings.REDIS_HASH_SYSTEM_AUTH_VALID_USERNAMES, db_user["username"]
        )

    return {"message": "User deleted from the database"}


@router.get(
    "/admin/users/{user_id}/rate-limits",
    dependencies=[Depends(get_current_superuser)],
)
async def read_user_rate_limits(
    request: Request,
    user_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, Any]:
    db_user = await crud_users.get(db=db, id=user_id, schema_to_select=UserRead)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    if db_user["tier_id"] is None:
        db_user["tier_rate_limits"] = []
        return db_user

    db_tier = await crud_tiers.get(db=db, id=db_user["tier_id"])
    if db_tier is None:
        raise NotFoundException(detail="Tier not found")

    db_rate_limits = await crud_rate_limits.get_multi(db=db, tier_id=db_tier["id"])

    db_user["tier_rate_limits"] = db_rate_limits["data"]

    return db_user


@router.get("/admin/users/{user_id}/tier")
async def read_user_tier(
    request: Request,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    user_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> dict | None:
    db_user = await crud_users.get(db=db, id=user_id, schema_to_select=UserRead)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    db_tier = await crud_tiers.exists(db=db, id=db_user["tier_id"])
    if not db_tier:
        raise NotFoundException(
            detail="Current user tier not found. Please update user tier first."
        )

    joined = await crud_users.get_joined(
        db=db,
        join_model=Tier,
        join_prefix="tier_",
        schema_to_select=UserRead,
        join_schema_to_select=TierRead,
        username=db_user["username"],
    )

    return joined


@router.patch(
    "/admin/users/{user_id}/tier",
    dependencies=[Depends(get_current_superuser)],
)
async def patch_user_tier(
    request: Request,
    user_id: UUID,
    values: UserTierUpdate,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_user = await crud_users.get(db=db, id=user_id, schema_to_select=UserRead)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    db_tier = await crud_tiers.get(db=db, id=values.tier_id)
    if db_tier is None:
        raise NotFoundException(detail="Tier not found")

    await crud_users.update(db=db, object=values, id=user_id)
    return {
        "message": f"User '{db_user['username']}' have been assigned to '{db_tier['name']}' tier."
    }
