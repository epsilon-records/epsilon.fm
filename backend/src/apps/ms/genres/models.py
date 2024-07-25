# Third-Party Dependencies
from sqlmodel import Field

# Local Dependencies
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, Base


class GenreContentBase(Base):
    genre_name: str = Field(
        max_length=255,
        nullable=False,
        description="Genre Name",
        schema_extra={"examples": ["Electronic"]},
    )


class Genre(
    UUIDMixin,
    GenreContentBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_genre"
    __table_args__ = ({"comment": "Management System genre information"},)
