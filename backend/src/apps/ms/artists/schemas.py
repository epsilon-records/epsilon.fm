# Built-in Dependencies

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.ms.artists.models import (
    ArtistProfileBase,
    ArtistMediaBase,
)
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin, OrgMixin
from src.core.utils.partial import optional


class ArtistBase(ArtistProfileBase, ArtistMediaBase):
    pass


class Artist(
    ArtistBase,
    OrgMixin,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
):
    pass


class ArtistCreate(ArtistBase):
    model_config = ConfigDict(extra="forbid")


@optional()
class ArtistUpdate(ArtistBase):
    model_config = ConfigDict(extra="forbid")


class ArtistDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
