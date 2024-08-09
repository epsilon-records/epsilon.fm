# Third-Party Dependencies
from sqlmodel import Field

# Local Dependencies
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, Base


class ReleaseContentBase(Base):
    release_name: str = Field(
        max_length=255,
        nullable=False,
        description="Release Name",
        schema_extra={"examples": ["Electronic"]},
    )


class Release(
    UUIDMixin,
    ReleaseContentBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_release"
    __table_args__ = ({"comment": "Management System release information"},)
