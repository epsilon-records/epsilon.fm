# Third-Party Dependencies
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

# Local Dependencies
from src.core.config import settings

# Define the database URI and URL based on the application settings
DATABASE_URI = f"{settings.POSTGRES_ASYNC_URI}"
DATABASE_URL = DATABASE_URI

# Create an async database engine
async_engine = create_async_engine(
    DATABASE_URL, echo=False, poolclass=NullPool, future=True
)

# Create a local session class using the async engine
local_session = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)  # type: ignore


# Define an async function to get the database session
async def async_get_db() -> AsyncSession:
    async_session = local_session

    async with async_session() as db:
        yield db
        await db.commit()
