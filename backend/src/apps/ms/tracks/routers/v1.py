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
from src.apps.ms.tracks.crud import crud_tracks
from src.core.db.session import async_get_db
from src.core.utils.cache import cache
from src.core.exceptions.http_exceptions import (
    NotFoundException,
    ForbiddenException,
)
from src.apps.ms.tracks.schemas import (
    Track,
    TrackCreate,
    TrackUpdate,
    TrackRead,
    TrackCreateInternal,
)
from src.core.utils.paginated import (
    PaginatedListResponse,
    paginated_response,
    compute_offset,
)

# TODO: Improvment the cache strategy on composite routes. Eg: '/epsilon/tracks/{track_id}/user/{user_id}' is not good.

router = fastapi.APIRouter(tags=["Epsilon - Tracks"])


@router.post(
    "/epsilon/tracks/user/{user_id}", response_model=TrackRead, status_code=201
)
async def write_track(
    request: Request,
    user_id: UUID,
    track: TrackCreate,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> TrackRead:
    db_user = await crud_users.get(
        db=db, schema_to_select=UserRead, id=user_id, is_deleted=False
    )
    if db_user is None:
        raise NotFoundException(detail="User not found")

    if current_user["id"] != db_user["id"]:
        raise ForbiddenException(
            detail="You are not allowed to create an track for this user"
        )

    # Prepare the track data
    track_internal_dict = track.model_dump()
    track_internal_dict["user_id"] = current_user["id"]

    track_internal = TrackCreateInternal(**track_internal_dict)
    return await crud_tracks.create(db=db, object=track_internal)


@router.get(
    "/epsilon/tracks/user/{user_id}", response_model=PaginatedListResponse[TrackRead]
)
@cache(
    key_prefix="epsilon:tracks:user:{user_id}:page_{page}:items_per_page:{items_per_page}",
    resource_id_name="user_id",
    expiration=60,
)
async def read_tracks(
    request: Request,
    user_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
    page: int = 1,
    items_per_page: int = 10,
) -> dict:
    db_user = await crud_users.get(
        db=db, schema_to_select=UserRead, id=user_id, is_deleted=False
    )
    if not db_user:
        raise NotFoundException(detail="User not found")

    tracks_data = await crud_tracks.get_multi(
        db=db,
        offset=compute_offset(page, items_per_page),
        limit=items_per_page,
        schema_to_select=TrackRead,
        user_id=db_user["id"],
        is_deleted=False,
    )

    return paginated_response(
        crud_data=tracks_data, page=page, items_per_page=items_per_page
    )


@router.get("/epsilon/tracks/{track_id}/user/{user_id}", response_model=TrackRead)
@cache(
    key_prefix="epsilon:tracks:user:{user_id}:track_cache", resource_id_name="track_id"
)
async def read_track(
    request: Request,
    user_id: UUID,
    track_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> dict:
    db_user = await crud_users.get(
        db=db, schema_to_select=UserRead, id=user_id, is_deleted=False
    )
    if db_user is None:
        raise NotFoundException(detail="User not found")

    db_track = await crud_tracks.get(
        db=db,
        schema_to_select=TrackRead,
        id=track_id,
        user_id=db_user["id"],
        is_deleted=False,
    )
    if db_track is None:
        raise NotFoundException(detail="Track not found")

    return db_track


@router.patch("/epsilon/tracks/{track_id}/user/{user_id}")
@cache(
    "epsilon:tracks:user:{user_id}:track_cache",
    resource_id_name="track_id",
    pattern_to_invalidate_extra=["epsilon:tracks:user:{user_id}:*"],
)
async def patch_track(
    request: Request,
    user_id: UUID,
    track_id: UUID,
    values: TrackUpdate,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_user = await crud_users.get(
        db=db, schema_to_select=UserRead, id=user_id, is_deleted=False
    )
    if db_user is None:
        raise NotFoundException(detail="User not found")

    if str(db_user["id"]) != str(current_user["id"]):
        raise ForbiddenException(detail="You are not allowed to update this track")

    db_track = await crud_tracks.get(
        db=db, schema_to_select=TrackRead, id=track_id, is_deleted=False
    )
    if db_track is None:
        raise NotFoundException(detail="Track not found")

    await crud_tracks.update(db=db, object=values, id=track_id)
    return {"message": "Track updated"}


@router.delete("/epsilon/tracks/{track_id}/user/{user_id}")
@cache(
    "epsilon:tracks:user:{user_id}:track_cache",
    resource_id_name="track_id",
    pattern_to_invalidate_extra=["epsilon:tracks:user:{user_id}:*"],
)
async def erase_track(
    request: Request,
    user_id: UUID,
    track_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_user = await crud_users.get(
        db=db, schema_to_select=UserRead, id=user_id, is_deleted=False
    )
    if db_user is None:
        raise NotFoundException(detail="User not found")

    if not current_user["is_superuser"] and str(current_user["id"]) != str(
        db_user["id"]
    ):
        raise ForbiddenException(detail="You are not allowed to delete this track")

    db_track = await crud_tracks.get(
        db=db, schema_to_select=Track, id=track_id, is_deleted=False
    )
    if db_track is None or db_track["is_deleted"]:
        if current_user["is_superuser"]:
            raise NotFoundException(detail="Track already deleted (soft delete).")
        raise NotFoundException(detail="Track not found")

    await crud_tracks.delete(db=db, db_row=db_track, id=track_id)

    return {"message": "Track deleted"}


@router.delete(
    "/epsilon/tracks/{track_id}/user/{user_id}/db",
    dependencies=[Depends(get_current_superuser)],
)
@cache(
    "epsilon:tracks:user:{user_id}:track_cache",
    resource_id_name="track_id",
    pattern_to_invalidate_extra=["epsilon:tracks:user:{user_id}:*"],
)
async def erase_db_track(
    request: Request,
    user_id: UUID,
    track_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_user = await crud_users.get(
        db=db, schema_to_select=UserRead, id=user_id, is_deleted=False
    )
    if db_user is None:
        raise NotFoundException(detail="User not found")

    db_track = await crud_tracks.get(db=db, schema_to_select=TrackRead, id=track_id)
    if db_track is None:
        raise NotFoundException(detail="Track not found")

    await crud_tracks.db_delete(db=db, id=track_id)
    return {"message": "Track deleted from the database"}
