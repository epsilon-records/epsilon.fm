# Third-Party Dependencies
from fastapi import APIRouter
from fastcrud import crud_router


# Local Dependencies
from src.core.db.session import async_get_db
from src.apps.auth.routers.v1 import router as auth_router
from src.apps.ms.artists.routers.v1 import router as artist_router
from src.apps.ms.artists.models import Artist
from src.apps.ms.tracks.models import Track
from src.apps.ms.genres.models import Genre
from src.apps.ms.subgenres.models import Subgenre
from src.apps.ms.releases.models import Release
from src.apps.ms.labels.models import Label
from src.apps.ms.releases.schemas import ReleaseCreate, ReleaseUpdate, ReleaseDelete
from src.apps.ms.labels.schemas import LabelCreate, LabelUpdate, LabelDelete
from src.apps.ms.artists.schemas import (
    ArtistCreate,
    ArtistUpdate,
    ArtistDelete,
)

from src.apps.ms.tracks.schemas import (
    TrackCreate,
    TrackUpdate,
    TrackDelete,
)

from src.apps.ms.genres.schemas import (
    GenreCreate,
    GenreUpdate,
    GenreDelete,
)

from src.apps.ms.subgenres.schemas import (
    SubgenreCreate,
    SubgenreUpdate,
    SubgenreDelete,
)

# Create an APIRouter instance for versioning and prefixing routes
api_v1_router = APIRouter(prefix="/v1")

# Include routers for different modules and functionalities under the v1 API version
api_v1_router.include_router(auth_router)
api_v1_router.include_router(artist_router)
api_v1_router.include_router(
    crud_router(
        session=async_get_db,
        model=Artist,
        create_schema=ArtistCreate,
        update_schema=ArtistUpdate,
        delete_schema=ArtistDelete,
        path="/artists",
        tags=["Artists"],
        included_methods=["create", "read", "read_multi", "update", "delete"],
        endpoint_names={
            "create": "",
            "read": "",
            "update": "",
            "delete": "",
            "db_delete": "",
            "read_multi": "",
            "read_paginated": "",
        },
    )
)
api_v1_router.include_router(
    crud_router(
        session=async_get_db,
        model=Track,
        create_schema=TrackCreate,
        update_schema=TrackUpdate,
        delete_schema=TrackDelete,
        path="/tracks",
        tags=["Tracks"],
        included_methods=["create", "read", "read_multi", "update", "delete"],
        endpoint_names={
            "create": "",
            "read": "",
            "update": "",
            "delete": "",
            "db_delete": "",
            "read_multi": "",
            "read_paginated": "",
        },
    )
)
api_v1_router.include_router(
    crud_router(
        session=async_get_db,
        model=Genre,
        create_schema=GenreCreate,
        update_schema=GenreUpdate,
        delete_schema=GenreDelete,
        path="/genres",
        tags=["Genres"],
        included_methods=["create", "read", "read_multi", "update", "delete"],
        endpoint_names={
            "create": "",
            "read": "",
            "update": "",
            "delete": "",
            "db_delete": "",
            "read_multi": "",
            "read_paginated": "",
        },
    )
)
api_v1_router.include_router(
    crud_router(
        session=async_get_db,
        model=Subgenre,
        create_schema=SubgenreCreate,
        update_schema=SubgenreUpdate,
        delete_schema=SubgenreDelete,
        path="/subgenres",
        tags=["Subgenres"],
        included_methods=["create", "read", "read_multi", "update", "delete"],
        endpoint_names={
            "create": "",
            "read": "",
            "update": "",
            "delete": "",
            "db_delete": "",
            "read_multi": "",
            "read_paginated": "",
        },
    )
)
api_v1_router.include_router(
    crud_router(
        session=async_get_db,
        model=Release,
        create_schema=ReleaseCreate,
        update_schema=ReleaseUpdate,
        delete_schema=ReleaseDelete,
        path="/releases",
        tags=["Releases"],
        included_methods=["create", "read", "read_multi", "update", "delete"],
        endpoint_names={
            "create": "",
            "read": "",
            "update": "",
            "delete": "",
            "db_delete": "",
            "read_multi": "",
            "read_paginated": "",
        },
    )
)
api_v1_router.include_router(
    crud_router(
        session=async_get_db,
        model=Label,
        create_schema=LabelCreate,
        update_schema=LabelUpdate,
        delete_schema=LabelDelete,
        path="/labels",
        tags=["Labels"],
        included_methods=["create", "read", "read_multi", "update", "delete"],
        endpoint_names={
            "create": "",
            "read": "",
            "update": "",
            "delete": "",
            "db_delete": "",
            "read_multi": "",
            "read_paginated": "",
        },
    )
)
