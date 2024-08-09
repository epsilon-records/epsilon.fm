# Third-Party Dependencies
from fastapi import APIRouter
from fastcrud import crud_router

# Local Dependencies
from src.core.db.session import async_get_db
from src.apps.auth.routers.v1 import router as auth_router
from src.apps.ms.artists.models import Artist
from src.apps.ms.artists.schemas import ArtistCreateInternal, ArtistUpdateInternal
from src.apps.ms.tracks.models import Track
from src.apps.ms.tracks.schemas import TrackCreateInternal, TrackUpdateInternal
from src.apps.ms.genres.models import Genre
from src.apps.ms.genres.schemas import GenreCreateInternal, GenreUpdateInternal
from src.apps.ms.subgenres.models import Subgenre
from src.apps.ms.subgenres.schemas import SubgenreCreateInternal, SubgenreUpdateInternal

# Create an APIRouter instance for versioning and prefixing routes
api_v1_router = APIRouter(prefix="/v1")

# Include routers for different modules and functionalities under the v1 API version
api_v1_router.include_router(auth_router)
api_v1_router.include_router(
    crud_router(
        session=async_get_db,
        model=Artist,
        create_schema=ArtistCreateInternal,
        update_schema=ArtistUpdateInternal,
        path="/artists",
        tags=["Artists"],
        # included_methods=["create", "read", "read_multiple", "update", "delete"],
    )
)
api_v1_router.include_router(
    crud_router(
        session=async_get_db,
        model=Track,
        create_schema=TrackCreateInternal,
        update_schema=TrackUpdateInternal,
        path="/tracks",
        tags=["Tracks"],
        # included_methods=["create", "read", "read_multiple", "update", "delete"],
    )
)
api_v1_router.include_router(
    crud_router(
        session=async_get_db,
        model=Genre,
        create_schema=GenreCreateInternal,
        update_schema=GenreUpdateInternal,
        path="/genres",
        tags=["Genres"],
        # included_methods=["create", "read", "read_multiple", "update", "delete"],
    )
)
api_v1_router.include_router(
    crud_router(
        session=async_get_db,
        model=Subgenre,
        create_schema=SubgenreCreateInternal,
        update_schema=SubgenreUpdateInternal,
        path="/subgenres",
        tags=["Subgenres"],
        # included_methods=["create", "read", "read_multiple", "update", "delete"],
    )
)
