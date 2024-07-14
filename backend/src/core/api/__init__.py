# Third-Party Dependencies
from fastapi import APIRouter

# Local Dependencies
from src.core.api.v1 import api_v1_router as v1_router

# Create an APIRouter instance for versioning and prefixing routes
router = APIRouter(prefix="/api")

# Include the routes defined in the v1_router (API version 1) into the main router
router.include_router(v1_router)
