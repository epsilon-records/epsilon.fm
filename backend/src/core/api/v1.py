# Third-Party Dependencies
from fastapi import APIRouter
from fastcrud import crud_router

# Local Dependencies
from src.core.db.session import async_get_db
from src.apps.auth.routers.v1 import router as auth_router
from src.apps.system.tiers.routers.v1 import router as tiers_router
from src.apps.system.rate_limits.routers.v1 import router as rate_limits_router
from src.apps.admin.users.routers.v1 import router as users_router
from src.apps.admin.tasks.routers.v1 import router as tasks_router
from src.apps.blog.posts.routers.v1 import router as posts_router
from src.apps.ms.artists.routers.v1 import router as artists_router
from src.apps.system.utils.routers.v1 import router as utils_router
from src.apps.ms.tracks.models import Track
from src.apps.ms.tracks.schemas import Track as TrackSchema

# Create an APIRouter instance for versioning and prefixing routes
api_v1_router = APIRouter(prefix="/v1")

# Include routers for different modules and functionalities under the v1 API version
api_v1_router.include_router(auth_router)
api_v1_router.include_router(tiers_router)
api_v1_router.include_router(rate_limits_router)
api_v1_router.include_router(users_router)
api_v1_router.include_router(tasks_router)
api_v1_router.include_router(posts_router)
api_v1_router.include_router(artists_router)
api_v1_router.include_router(utils_router)
api_v1_router.include_router(
    crud_router(
        session=async_get_db,
        model=Track,
        create_schema=TrackSchema,
        update_schema=TrackSchema,
        path="/tracks",
        tags=["Tracks"],
    )
)
