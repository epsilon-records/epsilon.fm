# Built-in Dependencies

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.ms.tracks.models import TrackContentBase, TrackMediaBase, TrackUserBase
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional


class TrackBase(TrackContentBase):
    pass


class Track(
    TrackBase, TrackMediaBase, TrackUserBase, UUIDMixin, TimestampMixin, SoftDeleteMixin
):
    pass


class TrackCreate(TrackBase, TrackMediaBase):
    model_config = ConfigDict(extra="forbid")


@optional()
class TrackUpdate(TrackContentBase, TrackMediaBase):
    model_config = ConfigDict(extra="forbid")


class TrackDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
