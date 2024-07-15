# Built-in Dependencies
from typing import Annotated, Dict
from uuid import UUID

# Third-Party Dependencies
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Request, Depends
import fastapi

# Local Dependencies
from src.core.api.dependencies import get_current_user, get_current_superuser
from src.apps.admin.users.schemas import UserRead
from src.apps.admin.users.crud import crud_users
from src.apps.epsilon.artists.crud import crud_artists
from src.core.db.session import async_get_db
from src.core.utils.cache import cache
from src.core.exceptions.http_exceptions import (
    NotFoundException,
    ForbiddenException,
)
from src.apps.epsilon.artists.schemas import (
    Artist,
    ArtistCreate,
    ArtistUpdate,
    ArtistRead,
    ArtistCreateInternal,
)
from src.core.utils.paginated import (
    PaginatedListResponse,
    paginated_response,
    compute_offset,
)

# TODO: Improvment the cache strategy on composite routes. Eg: '/epsilon/artists/{artist_id}/user/{user_id}' is not good.

router = fastapi.APIRouter(tags=["Epsilon - Artists"])


@router.post("/epsilon/artists/user/{user_id}", response_model=ArtistRead, status_code=201)
async def write_artist(
    request: Request,
    user_id: UUID,
    artist: ArtistCreate,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> ArtistRead:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    if current_user["id"] != db_user["id"]:
        raise ForbiddenException(detail="You are not allowed to create an artist for this user")

    # Prepare the artist data
    artist_internal_dict = artist.model_dump()
    artist_internal_dict["user_id"] = current_user["id"]

    artist_internal = ArtistCreateInternal(**artist_internal_dict)
    return await crud_artists.create(db=db, object=artist_internal)


@router.get("/artists", response_model=PaginatedListResponse[UserRead])
async def read_artists(
    request: Request,
    current_user: Annotated[ArtistRead],
    db: Annotated[AsyncSession, Depends(async_get_db)],
    page: int = 1,
    items_per_page: int = 10,
) -> dict:
    artists_data = await crud_artists.get_multi(
        db=db,
        offset=compute_offset(page, items_per_page),
        limit=items_per_page,
        schema_to_select=ArtistRead,
        is_deleted=False,
    )

    return paginated_response(crud_data=artists_data, page=page, items_per_page=items_per_page)

@router.get("/epsilon/artists/user/{user_id}", response_model=PaginatedListResponse[ArtistRead])
@cache(
    key_prefix="epsilon:artists:user:{user_id}:page_{page}:items_per_page:{items_per_page}",
    resource_id_name="user_id",
    expiration=60,
)
async def read_artists(
    request: Request,
    user_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
    page: int = 1,
    items_per_page: int = 10,
) -> dict:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if not db_user:
        raise NotFoundException(detail="User not found")

    artists_data = await crud_artists.get_multi(
        db=db,
        offset=compute_offset(page, items_per_page),
        limit=items_per_page,
        schema_to_select=ArtistRead,
        user_id=db_user["id"],
        is_deleted=False,
    )

    return paginated_response(crud_data=artists_data, page=page, items_per_page=items_per_page)


@router.get("/epsilon/artists/{artist_id}/user/{user_id}", response_model=ArtistRead)
@cache(key_prefix="epsilon:artists:user:{user_id}:artist_cache", resource_id_name="artist_id")
async def read_artist(
    request: Request,
    user_id: UUID,
    artist_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> dict:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    db_artist = await crud_artists.get(
        db=db,
        schema_to_select=ArtistRead,
        id=artist_id,
        user_id=db_user["id"],
        is_deleted=False,
    )
    if db_artist is None:
        raise NotFoundException(detail="Artist not found")

    return db_artist


@router.patch("/epsilon/artists/{artist_id}/user/{user_id}")
@cache(
    "epsilon:artists:user:{user_id}:artist_cache",
    resource_id_name="artist_id",
    pattern_to_invalidate_extra=["epsilon:artists:user:{user_id}:*"],
)
async def patch_artist(
    request: Request,
    user_id: UUID,
    artist_id: UUID,
    values: ArtistUpdate,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    if str(db_user["id"]) != str(current_user["id"]):
        raise ForbiddenException(detail="You are not allowed to update this artist")

    db_artist = await crud_artists.get(
        db=db, schema_to_select=ArtistRead, id=artist_id, is_deleted=False
    )
    if db_artist is None:
        raise NotFoundException(detail="Artist not found")

    await crud_artists.update(db=db, object=values, id=artist_id)
    return {"message": "Artist updated"}


@router.delete("/epsilon/artists/{artist_id}/user/{user_id}")
@cache(
    "epsilon:artists:user:{user_id}:artist_cache",
    resource_id_name="artist_id",
    pattern_to_invalidate_extra=["epsilon:artists:user:{user_id}:*"],
)
async def erase_artist(
    request: Request,
    user_id: UUID,
    artist_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    if not current_user["is_superuser"] and str(current_user["id"]) != str(db_user["id"]):
        raise ForbiddenException(detail="You are not allowed to delete this artist")

    db_artist = await crud_artists.get(
        db=db, schema_to_select=Artist, id=artist_id, is_deleted=False
    )
    if db_artist is None or db_artist["is_deleted"]:
        if current_user["is_superuser"]:
            raise NotFoundException(detail="Artist already deleted (soft delete).")
        raise NotFoundException(detail="Artist not found")

    await crud_artists.delete(db=db, db_row=db_artist, id=artist_id)

    return {"message": "Artist deleted"}


@router.delete(
    "/epsilon/artists/{artist_id}/user/{user_id}/db",
    dependencies=[Depends(get_current_superuser)],
)
@cache(
    "epsilon:artists:user:{user_id}:artist_cache",
    resource_id_name="artist_id",
    pattern_to_invalidate_extra=["epsilon:artists:user:{user_id}:*"],
)
async def erase_db_artist(
    request: Request,
    user_id: UUID,
    artist_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    db_artist = await crud_artists.get(db=db, schema_to_select=ArtistRead, id=artist_id)
    if db_artist is None:
        raise NotFoundException(detail="Artist not found")

    await crud_artists.db_delete(db=db, id=artist_id)
    return {"message": "Artist deleted from the database"}