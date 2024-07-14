# Built-in Dependencies
from datetime import datetime, UTC
from uuid import UUID, uuid4
from typing import Optional, Any

# Third-Party Dependencies
from sqlmodel import SQLModel, Field, DateTime
from pydantic import field_serializer


class Base(SQLModel):
    """
    Description:
    ----------
    Main base class for generating Pydantic models and database tables with SQLModel.
    """

    pass


class UUIDMixin(SQLModel):
    """
    Description:
    ----------
    'UUIDMixin' SQLModel base class.

    Fields:
    ----------
    - 'id': Unique identifier (UUID) for the record.
    """

    # Data Columns
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        description="Unique identifier (UUID) for the record",
    )


class TimestampMixin(SQLModel):
    """
    Description:
    ----------
    'TimestampMixin' SQLModel base class.

    Fields:
    ----------
    - 'created_at': Timestamp for the creation of the record.
    - 'updated_at': Timestamp for the last update of the record.

    Extra Info:
    ----------
    Adds 'created_at' and 'updated_at' fields with default values for the creation timestamp and update timestamp.

    Note: By default, 'updated_at' is set to the current timestamp on every update, which is useful for tracking the last
    modification time. However, in scenarios where soft deletion is performed and records may be restored, you might want
    to consider the following options:

    ----------------------------------------------------------

    Option 1 (Recommended for most scenarios):
    - Pros:
        - Keeps 'updated_at' always up-to-date, providing an accurate timestamp for the last modification.
        - Suitable for most use cases where soft deletion is not a common scenario.

    - Cons:
        - May lead to inaccurate information if soft deletion and restoration are part of the system's workflow.

    updated_at: datetime = Field(
        sa_type=DateTime(timezone=True),
        default_factory=lambda: datetime.now(UTC),
        sa_column_kwargs={"onupdate": datetime.now(UTC)},
        description="Timestamp for the last update of the record",
    )

    ----------------------------------------------------------

    Option 2 (Recommended for scenarios with frequent soft deletions and restorations):
    - Pros:
        - Preserves the original timestamp of the last real modification even after a soft delete and restore.
        - Avoids potential inaccuracies caused by automatic updates to 'updated_at' during soft deletions.

    - Cons:
        - 'updated_at' will not be automatically updated on every change, potentially affecting accuracy if the field
        needs to reflect every modification.
        - Currently, the BaseCRUD's update method in the API automatically handles the update of 'updated_at'. If other
        update methods are used that do not go through this mechanism, 'updated_at' may not be updated as expected.

    updated_at: Optional[datetime] = Field(
        sa_type=DateTime(timezone=True),
        default_factory=lambda: datetime.now(UTC),
        description="Timestamp for the last update of the record",
    )
    """

    created_at: datetime = Field(
        sa_type=DateTime(timezone=True),
        default_factory=lambda: datetime.now(UTC),
        description="Timestamp for the creation of the record",
    )
    updated_at: datetime = Field(
        sa_type=DateTime(timezone=True),
        default_factory=lambda: datetime.now(UTC),
        sa_column_kwargs={"onupdate": datetime.now(UTC)},
        description="Timestamp for the last update of the record",
    )

    @field_serializer("created_at")
    def serialize_dt(self, created_at: datetime | None, _info: Any) -> str | None:
        if created_at is not None:
            return created_at.isoformat()

        return None

    @field_serializer("updated_at")
    def serialize_updated_at(self, updated_at: datetime | None, _info: Any) -> str | None:
        if updated_at is not None:
            return updated_at.isoformat()

        return None


class SoftDeleteMixin(SQLModel):
    """
    Description:
    ----------
    'SoftDeleteMixin' SQLModel base class.

    Fields:
    ----------
    - 'deleted_at': Timestamp for the deletion of the record (soft deletion).
    - 'is_deleted': Flag indicating whether the record is deleted (soft deletion).

    Extra Info:
    ----------
    Adds 'deleted_at' and 'is_deleted' fields for soft deletion functionality.
    """

    # Data Columns
    deleted_at: Optional[datetime] = Field(
        sa_type=DateTime(timezone=True),
        default=None,
        description="Timestamp for the deletion of the record (soft deletion)",
    )
    is_deleted: bool = Field(
        default=False,
        index=True,
        description="Flag indicating whether the record is deleted (soft deletion)",
    )

    @field_serializer("deleted_at")
    def serialize_dates(self, deleted_at: datetime | None, _info: Any) -> str | None:
        if deleted_at is not None:
            return deleted_at.isoformat()

        return None
