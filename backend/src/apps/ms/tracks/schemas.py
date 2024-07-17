# Built-in Dependencies
from datetime import datetime

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.e.tracks.models import TrackContentBase, TrackMediaBase, TrackUserBase
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional


class TrackBase(TrackContentBase):
    pass


class Track(TrackBase, TrackMediaBase, TrackUserBase, UUIDMixin, TimestampMixin, SoftDeleteMixin):
    pass


class TrackRead(TrackBase, TrackMediaBase, TrackUserBase, UUIDMixin, TimestampMixin):
    pass


class TrackCreate(TrackBase, TrackMediaBase):
    model_config = ConfigDict(extra="forbid")


class TrackCreateInternal(TrackCreate, TrackUserBase):
    pass


@optional()
class TrackUpdate(TrackContentBase, TrackMediaBase):
    model_config = ConfigDict(extra="forbid")


class TrackUpdateInternal(TrackUpdate):
    updated_at: datetime


class TrackDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
