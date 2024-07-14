# Built-in Dependencies
from typing import Annotated, Dict
from uuid import UUID

# Third-Party Dependencies
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import Request, Depends
import fastapi

# Local Dependencies
from src.core.api.dependencies import get_current_user, get_current_superuser
from src.apps.admin.users.schemas import UserRead
from src.apps.system.tiers.crud import crud_tiers
from src.core.db.session import async_get_db
from src.core.exceptions.http_exceptions import (
    DuplicateValueException,
    ForbiddenException,
    NotFoundException,
)
from src.apps.system.tiers.schemas import (
    TierRead,
    TierCreate,
    TierCreateInternal,
    TierUpdate,
)
from src.core.utils.paginated import (
    PaginatedListResponse,
    paginated_response,
    compute_offset,
)
from src.core.config import settings

router = fastapi.APIRouter(tags=["System - Tiers"])


@router.post(
    "/system/tiers",
    dependencies=[Depends(get_current_superuser)],
    status_code=201,
)
async def write_tier(
    request: Request,
    tier: TierCreate,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> TierRead:
    tier_internal_dict = tier.model_dump()
    db_tier = await crud_tiers.exists(db=db, name=tier_internal_dict["name"])
    if db_tier:
        raise DuplicateValueException(detail="Tier Name not available")

    tier_internal = TierCreateInternal(**tier_internal_dict)
    return await crud_tiers.create(db=db, object=tier_internal)


@router.get(
    "/system/tiers",
    response_model=PaginatedListResponse[TierRead],
)
async def read_tiers(
    request: Request,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
    page: int = 1,
    items_per_page: int = 10,
) -> dict:
    tiers_data = await crud_tiers.get_multi(
        db=db,
        offset=compute_offset(page, items_per_page),
        limit=items_per_page,
        schema_to_select=TierRead,
    )

    return paginated_response(crud_data=tiers_data, page=page, items_per_page=items_per_page)


@router.get(
    "/system/tiers/{tier_id}",
    response_model=TierRead,
)
async def read_tier(
    request: Request,
    tier_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> dict:
    db_tier = await crud_tiers.get(db=db, schema_to_select=TierRead, id=tier_id)
    if db_tier is None:
        raise NotFoundException(detail="Tier not found")

    return db_tier


@router.patch("/system/tiers/{tier_id}", dependencies=[Depends(get_current_superuser)])
async def patch_tier(
    request: Request,
    values: TierUpdate,
    tier_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_tier = await crud_tiers.get(db=db, schema_to_select=TierRead, id=tier_id)
    if db_tier is None:
        raise NotFoundException(detail="Tier not found")

    if db_tier["name"] == settings.TIER_NAME_DEFAULT:
        raise ForbiddenException(detail="Default Tier cannot be updated")

    await crud_tiers.update(db=db, object=values, id=tier_id)
    return {"message": "Tier updated"}


@router.delete("/system/tiers/{tier_id}", dependencies=[Depends(get_current_superuser)])
async def erase_tier(
    request: Request,
    tier_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_tier = await crud_tiers.get(db=db, schema_to_select=TierRead, id=tier_id)
    if db_tier is None:
        raise NotFoundException(detail="Tier not found")

    if db_tier["name"] == settings.TIER_NAME_DEFAULT:
        raise ForbiddenException(detail="Default Tier cannot be deleted")

    try:
        await crud_tiers.delete(db=db, db_row=db_tier, id=tier_id)
    except IntegrityError:
        raise ForbiddenException(detail="Tier cannot be deleted")

    return {"message": "Tier deleted"}
