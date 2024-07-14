# Built-in Dependencies
from logging.config import fileConfig
import asyncio

# Third-Party Dependencies
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy.engine import Connection
from sqlalchemy import pool
from alembic import context

# Local Dependencies
from src.core.common.models import Base
from src.core.config import settings
from src.core.db import *

# Define the custom Alembic version table name
custom_alembic_version_table_name = "_alembic_version"

# The Alembic Config object providing access to the .ini file values.
config = context.config

# Set the SQLAlchemy URL using the Postgres async URI from settings.
config.set_main_option(name="sqlalchemy.url", value=f"{settings.POSTGRES_ASYNC_URI}")

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

# Other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def filter_db_objects(
    object,  # noqa: indirect usage
    name,
    type_,
    *args,  # noqa: indirect usage
    **kwargs,  # noqa: indirect usage
):
    """
    Filter the database objects based on the given criteria.

    Args:
        object: The database object to be filtered. # noqa: indirect usage
        name: The name of the database object.
        type_: The type of the database object.
        *args: Additional positional arguments. # noqa: indirect usage
        **kwargs: Additional keyword arguments. # noqa: indirect usage

    Returns:
        bool: True if the object should be included, False if it should be filtered out.
    """
    if type_ == "index" and name.startswith("idx") and name.endswith("geom"):
        return False

    return True


def do_run_migrations(connection: Connection) -> None:
    """Perform the actual migration process.

    This function is responsible for running migrations when the application is connected to a database.
    """
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        version_table=custom_alembic_version_table_name,  # Change the alembic version table name
    )

    with context.begin_transaction():
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=filter_db_objects,
            version_table=custom_alembic_version_table_name,  # Change the alembic version table name
        )
        context.run_migrations()


async def run_async_migrations() -> None:
    """Run migrations asynchronously.

    This function is responsible for running migrations in an asynchronous manner.
    """
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
    """Run migrations in 'offline' mode.

    This configures the context with just a URL and not an Engine, though an Engine is acceptable here as well.
    By skipping the Engine creation, we don't even need a DBAPI to be available.

    This function is responsible for running migrations when the application is not connected to a database.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=filter_db_objects,
        version_table=custom_alembic_version_table_name,  # Change the alembic version table name
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    This function is responsible for running migrations when the application is online.
    """
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
