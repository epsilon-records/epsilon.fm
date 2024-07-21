# Built-in Dependencies
from datetime import datetime

# Third-Party Dependencies
from pydantic import ConfigDict
from sqlmodel import Field

# Local Dependencies
from src.apps.ms.artists.models import (
    ArtistContentBase,
    ArtistMediaBase,
    ArtistUserBase,
)
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional


class ArtistBase(ArtistContentBase):
    pass


class Artist(
    ArtistBase,
    ArtistMediaBase,
    ArtistUserBase,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
):
    pass


class ArtistDB(ArtistBase, ArtistMediaBase, UUIDMixin, TimestampMixin):
    pass


class ArtistRead(ArtistBase, ArtistMediaBase, UUIDMixin, TimestampMixin):
    slug: str = Field(default=None)
    stage_name: str = Field(default=None)
    __tablename__ = None
    model_config = ConfigDict(from_attributes=True)


class ArtistCreate(ArtistBase, ArtistMediaBase):
    model_config = ConfigDict(extra="forbid")


class ArtistCreateInternal(ArtistCreate, ArtistUserBase):
    pass


@optional()
class ArtistUpdate(ArtistContentBase, ArtistMediaBase):
    model_config = ConfigDict(extra="forbid")


class ArtistUpdateInternal(ArtistUpdate):
    updated_at: datetime


class ArtistDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
