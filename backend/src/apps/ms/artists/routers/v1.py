# Built-in Dependencies
from typing import Annotated

# Third-Party Dependencies
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Request, Depends
import fastapi

# Local Dependencies
from src.apps.ms.artists.crud import crud_artists
from src.core.db.session import async_get_db
from src.core.exceptions.http_exceptions import (
    NotFoundException,
)
from src.apps.ms.artists.schemas import (
    ArtistRead,
    ArtistDB,
)

router = fastapi.APIRouter(tags=["Artists"])


@router.get("/artists/{org_id}", response_model=ArtistRead)
async def read_artist(
    request: Request,
    org_id: str,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> dict:
    db_artist = await crud_artists.get(
        db=db,
        schema_to_select=ArtistDB,
        org_id=org_id,
        is_deleted=False,
    )
    if db_artist is None:
        raise NotFoundException(detail="Artist not found")
    db_artist["slug"] = "<slug>"
    db_artist["stage_name"] = "<stage_name>"
    return db_artist
