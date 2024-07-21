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
from src.apps.ms.artists.crud import crud_artists
from src.core.db.session import async_get_db
from src.core.utils.cache import cache
from src.core.exceptions.http_exceptions import (
    NotFoundException,
    ForbiddenException,
)
from src.apps.ms.artists.schemas import (
    Artist,
    ArtistCreate,
    ArtistUpdate,
    ArtistRead,
    ArtistDB,
    ArtistCreateInternal,
)
from src.core.utils.paginated import (
    PaginatedListResponse,
    paginated_response,
    compute_offset,
)

# TODO: Improvement the cache strategy on composite routes. Eg: '/artists/{artist_id}/user/{user_id}' is not good.

router = fastapi.APIRouter(tags=["Artists"])


@router.post("/artists/user/{user_id}", response_model=ArtistRead, status_code=201)
async def write_artist(
    request: Request,
    user_id: UUID,
    artist: ArtistCreate,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> ArtistRead:
    """
    Create a new artist for a specific user.

    This endpoint allows creating a new artist associated with a given user. The current user must have permission to create an artist for the specified user.

    Args:
        request (Request): The incoming request object.
        user_id (UUID): The ID of the user for whom the artist is being created.
        artist (ArtistCreate): The artist data to be created.
        current_user (UserRead): The current authenticated user.
        db (AsyncSession): The database session.

    Returns:
        ArtistRead: The created artist data.

    Raises:
        NotFoundException: If the specified user is not found.
        ForbiddenException: If the current user is not allowed to create an artist for the specified user.
    """
    db_user = await crud_users.get(
        db=db, schema_to_select=UserRead, id=user_id, is_deleted=False
    )
    if db_user is None:
        raise NotFoundException(detail="User not found")

    if current_user["id"] != db_user["id"]:
        raise ForbiddenException(
            detail="You are not allowed to create an artist for this user"
        )

    # Prepare the artist data
    artist_internal_dict = artist.model_dump()
    artist_internal_dict["user_id"] = current_user["id"]

    artist_internal = ArtistCreateInternal(**artist_internal_dict)
    return await crud_artists.create(db=db, object=artist_internal)


@router.get("/artists", response_model=PaginatedListResponse[ArtistRead])
async def read_artists(
    request: Request,
    db: Annotated[AsyncSession, Depends(async_get_db)],
    page: int = 1,
    items_per_page: int = 10,
) -> dict:
    """
    Retrieve a paginated list of artists.

    This endpoint returns a paginated list of all non-deleted artists in the database.

    Args:
        request (Request): The incoming request object.
        db (AsyncSession): The database session.
        page (int, optional): The page number for pagination. Defaults to 1.
        items_per_page (int, optional): The number of items per page. Defaults to 10.

    Returns:
        dict: A paginated response containing the list of artists.
    """
    artists_data = await crud_artists.get_multi(
        db=db,
        offset=compute_offset(page, items_per_page),
        limit=items_per_page,
        schema_to_select=ArtistDB,
        is_deleted=False,
    )
    for artist in artists_data:
        artist["slug"] = "<slug>"
        artist["stage_name"] = "<stage_name>"
    return paginated_response(
        crud_data=artists_data, page=page, items_per_page=items_per_page
    )


@router.get("/artists/{org_id}", response_model=ArtistRead)
async def read_artist(
    request: Request,
    org_id: str,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> dict:
    """
    Retrieve a specific artist by their organization ID.

    This endpoint returns the details of a specific artist based on their organization ID.

    Args:
        request (Request): The incoming request object.
        org_id (str): The organization ID of the artist.
        db (AsyncSession): The database session.

    Returns:
        dict: The artist data.

    Raises:
        NotFoundException: If the artist is not found.
    """
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


@router.patch("/artists/{artist_id}/user/{user_id}")
@cache(
    "artists:user:{user_id}:artist_cache",
    resource_id_name="artist_id",
    pattern_to_invalidate_extra=["e:artists:user:{user_id}:*"],
)
async def patch_artist(
    request: Request,
    user_id: UUID,
    artist_id: UUID,
    values: ArtistUpdate,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    """
    Update an existing artist.

    This endpoint allows updating the details of an existing artist. The current user must have permission to update the specified artist.

    Args:
        request (Request): The incoming request object.
        user_id (UUID): The ID of the user associated with the artist.
        artist_id (UUID): The ID of the artist to be updated.
        values (ArtistUpdate): The updated artist data.
        current_user (UserRead): The current authenticated user.
        db (AsyncSession): The database session.

    Returns:
        Dict[str, str]: A dictionary containing the message "Artist updated".

    Raises:
        NotFoundException: If the user or artist is not found.
        ForbiddenException: If the current user is not allowed to update the artist.
    """
    db_user = await crud_users.get(
        db=db, schema_to_select=UserRead, id=user_id, is_deleted=False
    )
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


@router.delete("/artists/{artist_id}/user/{user_id}")
@cache(
    "artists:user:{user_id}:artist_cache",
    resource_id_name="artist_id",
    pattern_to_invalidate_extra=["e:artists:user:{user_id}:*"],
)
async def erase_artist(
    request: Request,
    user_id: UUID,
    artist_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    """
    Delete an artist.

    This endpoint allows a user to delete an artist. The user must be authenticated and have the necessary permissions to perform the delete operation.

    Args:
        request (Request): The incoming request object.
        user_id (UUID): The ID of the user performing the delete operation.
        artist_id (UUID): The ID of the artist to be deleted.
        current_user (UserRead): The current authenticated user.
        db (AsyncSession): The database session.

    Returns:
        Dict[str, str]: A dictionary containing the message "Artist deleted".

    Raises:
        NotFoundException: If the user or artist is not found.
        ForbiddenException: If the current user is not allowed to delete the artist.
    """
    db_user = await crud_users.get(
        db=db, schema_to_select=UserRead, id=user_id, is_deleted=False
    )
    if db_user is None:
        raise NotFoundException(detail="User not found")

    if not current_user["is_superuser"] and str(current_user["id"]) != str(
        db_user["id"]
    ):
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
    "/artists/{artist_id}/user/{user_id}/db",
    dependencies=[Depends(get_current_superuser)],
)
@cache(
    "artists:user:{user_id}:artist_cache",
    resource_id_name="artist_id",
    pattern_to_invalidate_extra=["e:artists:user:{user_id}:*"],
)
async def erase_db_artist(
    request: Request,
    user_id: UUID,
    artist_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    """
    Permanently delete an artist from the database.

    This endpoint allows a superuser to permanently delete an artist from the database. This operation cannot be undone.

    Args:
        request (Request): The incoming request object.
        user_id (UUID): The ID of the user associated with the artist.
        artist_id (UUID): The ID of the artist to be deleted.
        db (AsyncSession): The database session.

    Returns:
        Dict[str, str]: A dictionary containing the message "Artist deleted from the database".

    Raises:
        NotFoundException: If the user or artist is not found.
    """
    db_user = await crud_users.get(
        db=db, schema_to_select=UserRead, id=user_id, is_deleted=False
    )
    if db_user is None:
        raise NotFoundException(detail="User not found")

    db_artist = await crud_artists.get(db=db, schema_to_select=ArtistRead, id=artist_id)
    if db_artist is None:
        raise NotFoundException(detail="Artist not found")

    await crud_artists.db_delete(db=db, id=artist_id)
    return {"message": "Artist deleted from the database"}
