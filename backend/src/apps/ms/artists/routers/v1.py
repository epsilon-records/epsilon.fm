# Built-in Dependencies
from typing import Annotated

# Third-Party Dependencies
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Request, Depends
import fastapi
from fastcrud import FastCRUD

# Local Dependencies
from src.apps.ms.artists.models import Artist
from src.core.db.session import async_get_db
from src.core.exceptions.http_exceptions import (
    NotFoundException,
)
from src.apps.ms.artists.schemas import (
    ArtistCreate,
    ArtistRead,
)

router = fastapi.APIRouter(tags=["Artists"])
artist_crud = FastCRUD(Artist)


@router.post("/artists", response_model=ArtistRead, status_code=201)
async def write_artist(
    request: Request,
    artist: ArtistCreate,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> ArtistRead:
    return await artist_crud.create(db=db, object=artist)


@router.get("/artists/{org_id}", response_model=ArtistRead)
async def read_artist(
    request: Request,
    org_id: str,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> dict:
    db_artist = await artist_crud.get(
        db=db,
        schema_to_select=ArtistRead,
        org_id=org_id,
        is_deleted=False,
    )
    if db_artist is None:
        raise NotFoundException(detail="Artist not found")
    return db_artist
