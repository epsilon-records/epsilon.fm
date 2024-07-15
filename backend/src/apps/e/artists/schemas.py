# Built-in Dependencies
from datetime import datetime

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.e.artists.models import ArtistContentBase, ArtistMediaBase, ArtistUserBase
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional


class ArtistBase(ArtistContentBase):
    pass


class Artist(
    ArtistBase, ArtistMediaBase, ArtistUserBase, UUIDMixin, TimestampMixin, SoftDeleteMixin
):
    pass


class ArtistRead(ArtistBase, ArtistMediaBase, ArtistUserBase, UUIDMixin, TimestampMixin):
    pass


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
