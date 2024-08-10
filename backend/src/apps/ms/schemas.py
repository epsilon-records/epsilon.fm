# Built-in Dependencies
from datetime import datetime

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.ms.albums.models import AlbumContentBase, AlbumMediaBase, AlbumUserBase
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional
from src.apps.ms.genres.models import GenreContentBase
from src.apps.ms.subgenres.models import SubgenreContentBase


class GenreBase(GenreContentBase):
    pass


class Genre(GenreBase, UUIDMixin, TimestampMixin, SoftDeleteMixin):
    pass


class GenreCreate(GenreBase):
    model_config = ConfigDict(extra="forbid")


@optional()
class GenreUpdate(GenreContentBase):
    model_config = ConfigDict(extra="forbid")


class GenreDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")


class SubgenreBase(SubgenreContentBase):
    pass


class Subgenre(
    SubgenreBase,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
):
    pass


class SubgenreCreate(
    SubgenreBase,
):
    model_config = ConfigDict(extra="forbid")


@optional()
class SubgenreUpdate(
    SubgenreContentBase,
):
    model_config = ConfigDict(extra="forbid")


class SubgenreDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")


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
