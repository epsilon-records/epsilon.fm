# Third-Party Dependencies
from sqlmodel import Field

# Local Dependencies
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, Base


class AlbumContentBase(Base):
    album_name: str = Field(
        max_length=255,
        nullable=False,
        description="Album Name",
        schema_extra={"examples": ["Electronic"]},
    )


class Album(
    UUIDMixin,
    AlbumContentBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_album"
    __table_args__ = ({"comment": "Management System album information"},)
