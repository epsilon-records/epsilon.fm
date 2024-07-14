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

router = fastapi.APIRouter(tags=["System - Utils"])


@router.get("/system/utils/ping", status_code=200)
async def ping() -> dict:
    return {"message": "pong"}
