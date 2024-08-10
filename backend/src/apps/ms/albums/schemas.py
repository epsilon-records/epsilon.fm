# Built-in Dependencies
from datetime import datetime

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.ms.models import AlbumContentBase, AlbumMediaBase, AlbumUserBase
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional


class AlbumBase(AlbumContentBase):
    pass


class Album(
    AlbumBase, AlbumMediaBase, AlbumUserBase, UUIDMixin, TimestampMixin, SoftDeleteMixin
):
    pass


class AlbumRead(AlbumBase, AlbumMediaBase, AlbumUserBase, UUIDMixin, TimestampMixin):
    pass


class AlbumCreate(AlbumBase, AlbumMediaBase):
    model_config = ConfigDict(extra="forbid")


class AlbumCreateInternal(AlbumCreate, AlbumUserBase):
    pass


@optional()
class AlbumUpdate(AlbumContentBase, AlbumMediaBase):
    model_config = ConfigDict(extra="forbid")


class AlbumUpdateInternal(AlbumUpdate):
    updated_at: datetime


class AlbumDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
