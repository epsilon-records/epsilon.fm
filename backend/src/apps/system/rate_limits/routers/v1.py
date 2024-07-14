# Built-in Dependencies
from typing import Annotated, Dict
from uuid import UUID

# Third-Party Dependencies
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Request, Depends
import fastapi

# Local Dependencies
from src.core.api.dependencies import get_current_superuser
from src.core.db.session import async_get_db
from src.apps.system.rate_limits.crud import crud_rate_limits
from src.apps.system.tiers.crud import crud_tiers
from src.core.utils.rate_limit import is_valid_path
from src.core.exceptions.http_exceptions import (
    UnprocessableEntityException,
    DuplicateValueException,
    RateLimitException,
    NotFoundException,
)
from src.apps.system.rate_limits.schemas import (
    RateLimitCreateInternal,
    RateLimitCreate,
    RateLimitUpdate,
    RateLimitRead,
)
from src.core.utils.paginated import (
    PaginatedListResponse,
    paginated_response,
    compute_offset,
)

router = fastapi.APIRouter(tags=["System - Rate Limits"])


@router.post(
    "/system/rate-limits/tier/{tier_id}",
    dependencies=[Depends(get_current_superuser)],
    status_code=201,
)
async def write_rate_limit(
    request: Request,
    tier_id: UUID,
    rate_limit: RateLimitCreate,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> RateLimitRead:
    db_tier = await crud_tiers.get(db=db, id=tier_id)
    if not db_tier:
        raise NotFoundException(detail="Tier not found")

    rate_limit_internal_dict = rate_limit.model_dump()
    rate_limit_internal_dict["tier_id"] = db_tier["id"]

    # Checks if the path is a valid route
    if not is_valid_path(path=rate_limit.path, app=request.app):
        raise UnprocessableEntityException(detail="Invalid path")

    db_rate_limit = await crud_rate_limits.exists(db=db, name=rate_limit_internal_dict["name"])
    if db_rate_limit:
        raise DuplicateValueException(detail="Rate Limit Name not available")

    rate_limit_internal = RateLimitCreateInternal(**rate_limit_internal_dict)
    return await crud_rate_limits.create(db=db, object=rate_limit_internal)


@router.get(
    "/system/rate-limits/tier/{tier_id}",
    dependencies=[Depends(get_current_superuser)],
    response_model=PaginatedListResponse[RateLimitRead],
)
async def read_rate_limits(
    request: Request,
    tier_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
    page: int = 1,
    items_per_page: int = 10,
) -> dict:
    db_tier = await crud_tiers.get(db=db, id=tier_id)
    if not db_tier:
        raise NotFoundException(detail="Tier not found")

    rate_limits_data = await crud_rate_limits.get_multi(
        db=db,
        offset=compute_offset(page, items_per_page),
        limit=items_per_page,
        schema_to_select=RateLimitRead,
        tier_id=tier_id,
    )

    return paginated_response(crud_data=rate_limits_data, page=page, items_per_page=items_per_page)


@router.get(
    "/system/rate-limits/{rate_limit_id}/tier/{tier_id}",
    dependencies=[Depends(get_current_superuser)],
    response_model=RateLimitRead,
)
async def read_rate_limit(
    request: Request,
    tier_id: UUID,
    rate_limit_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> dict:
    db_tier = await crud_tiers.get(db=db, id=tier_id)
    if not db_tier:
        raise NotFoundException(detail="Tier not found")

    db_rate_limit = await crud_rate_limits.get(
        db=db, schema_to_select=RateLimitRead, tier_id=tier_id, id=rate_limit_id
    )
    if db_rate_limit is None:
        raise NotFoundException(detail="Rate Limit not found")

    return db_rate_limit


@router.patch(
    "/system/rate-limits/{rate_limit_id}/tier/{tier_id}",
    dependencies=[Depends(get_current_superuser)],
)
async def patch_rate_limit(
    request: Request,
    tier_id: UUID,
    rate_limit_id: UUID,
    values: RateLimitUpdate,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_tier = await crud_tiers.get(db=db, id=tier_id)
    if db_tier is None:
        raise NotFoundException(detail="Tier not found")

    db_rate_limit = await crud_rate_limits.get(
        db=db, schema_to_select=RateLimitRead, tier_id=tier_id, id=rate_limit_id
    )
    if db_rate_limit is None:
        raise NotFoundException(detail="Rate Limit not found")

    if values.path is not None:
        # Checks if the path is a valid route
        if not is_valid_path(path=values.path, app=request.app):
            raise NotFoundException(detail="Invalid path")

        # Checks if there is already a rate limit for this path
        db_rate_limit_path = await crud_rate_limits.exists(db=db, tier_id=tier_id, path=values.path)
        if db_rate_limit_path:
            raise DuplicateValueException(detail="There is already a rate limit for this path")

    if values.name is not None:
        db_rate_limit_name = await crud_rate_limits.exists(
            db=db,
            name=values.name,
        )
        if db_rate_limit_name:
            raise DuplicateValueException(detail="There is already a rate limit with this name")

    await crud_rate_limits.update(db=db, object=values, id=rate_limit_id)
    return {"message": "Rate Limit updated"}


@router.delete(
    "/system/rate-limits/{rate_limit_id}/tier/{tier_id}",
    dependencies=[Depends(get_current_superuser)],
)
async def erase_rate_limit(
    request: Request,
    tier_id: UUID,
    rate_limit_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_tier = await crud_tiers.get(db=db, id=tier_id)
    if not db_tier:
        raise NotFoundException(detail="Tier not found")

    db_rate_limit = await crud_rate_limits.get(
        db=db, schema_to_select=RateLimitRead, tier_id=tier_id, id=rate_limit_id
    )
    if db_rate_limit is None:
        raise RateLimitException(detail="Rate Limit not found")

    await crud_rate_limits.delete(db=db, db_row=db_rate_limit, id=rate_limit_id)
    return {"message": "Rate Limit deleted"}
