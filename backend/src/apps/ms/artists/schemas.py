# Built-in Dependencies

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.ms.artists.models import (
    ArtistProfileBase,
    ArtistAnalyticsBase,
    ArtistMediaBase,
)
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, OrgMixin
from src.core.utils.partial import optional


class ArtistBase(ArtistProfileBase, ArtistAnalyticsBase, ArtistMediaBase):
    pass


class ArtistRead(ArtistBase, UUIDMixin, OrgMixin, TimestampMixin):
    pass


class ArtistCreate(ArtistBase):
    model_config = ConfigDict(extra="forbid")


@optional()
class ArtistUpdate(ArtistBase):
    model_config = ConfigDict(extra="forbid")


class ArtistDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
