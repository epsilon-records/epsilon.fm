# Local Dependencies
from src.core.setup import create_application
from src.core.config import settings
from src.core.api import router

# Set up FastAPI application
app = create_application(router=router, settings=settings)
