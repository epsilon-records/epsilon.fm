# Built-in Dependencies
from uuid import UUID
from typing import Optional

# Third-Party Dependencies
from sqlmodel import Field

# Local Dependencies
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, Base


class ArtistContentBase(Base):
    email: str = Field(max_length=255)
    biography: str = Field(
        max_length=1000,
        description="Artist Biography",
    )


class ArtistMediaBase(Base):
    media_url: Optional[str] = Field(
        max_length=255,
        nullable=True,
        default=None,
        regex=r"^(https?):\/\/[^\s\/$.?#].[^\s]*\.(jpg|jpeg|png|gif)$",
        description="URL of the media associated with the post",
    )


class ArtistOrgBase(Base):
    org_id: str = Field(
        description="Organization ID associated with the artist",
        max_length=255,
        unique=True,
    )


class ArtistAnalyticsBase(Base):
    soundcharts_artist_id: UUID = Field(
        description="Soundcharts Artist UUID associated with the artist",
        nullable=True,
        default=None,
        unique=True,
    )


class Artist(
    UUIDMixin,
    ArtistContentBase,
    ArtistOrgBase,
    ArtistAnalyticsBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_artist"
    __table_args__ = ({"comment": "Management System artist information"},)
