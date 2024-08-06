# Built-in Dependencies
from logging.config import fileConfig
import asyncio
import os

# Third-Party Dependencies
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy.engine import Connection
from sqlalchemy import pool
from alembic import context
from dotenv import load_dotenv

# Local Dependencies
from src.core.config import settings
from src.core.common.models import Base
import src.core.db  # noqa: F401

# Load environment variables from .env file
load_dotenv()

# Define the custom Alembic version table name
custom_alembic_version_table_name = "_alembic_version"

# The Alembic Config object providing access to the .ini file values.
config = context.config

# Set the SQLAlchemy URL using the Postgres async URI from settings
config.set_main_option(name="sqlalchemy.url", value=f"{settings.POSTGRES_ASYNC_URI}")

# Override with the database URL from environment variable if it exists
if "MIGRATE_DATABASE_URL" in os.environ:
    config.set_main_option(
        name="sqlalchemy.url", value=f"{os.environ['MIGRATE_DATABASE_URL']}"
    )
    print(
        f"Using database URL from environment variable: {os.environ['MIGRATE_DATABASE_URL']}"
    )

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Add your model's MetaData object here (for 'autogenerate' support)
target_metadata = Base.metadata

# Setting naming conventions for SQLModel/SQLAlchemy
target_metadata.naming_convention = {
    "ix": "ix_%(column_0_label)s",  # Index
    "uq": "uq_%(table_name)s_%(column_0_name)s",  # Unique constraint
    "ck": "ck_%(table_name)s_%(constraint_name)s",  # Check constraint
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",  # Foreign key
    "pk": "pk_%(table_name)s",  # Primary key
}


def filter_db_objects(
    object,
    name,
    type_,
    *args,
    **kwargs,
):
    if type_ == "index" and name.startswith("idx") and name.endswith("geom"):
        return False

    return True


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        version_table=custom_alembic_version_table_name,
    )

    with context.begin_transaction():
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=filter_db_objects,
            version_table=custom_alembic_version_table_name,
        )
        context.run_migrations()


async def run_async_migrations() -> None:
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        future=True,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=filter_db_objects,
        version_table=custom_alembic_version_table_name,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
