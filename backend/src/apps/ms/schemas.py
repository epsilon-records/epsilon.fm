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
from src.apps.ms.artists.models import (
    ArtistProfileBase,
    ArtistAnalyticsBase,
    ArtistMediaBase,
)
from src.core.common.models import OrgMixin
from src.apps.ms.releases.models import ReleaseContentBase
from src.apps.ms.tracks.models import TrackContentBase, TrackMediaBase, TrackUserBase


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


class ReleaseBase(ReleaseContentBase):
    pass


class Release(ReleaseBase, UUIDMixin, TimestampMixin, SoftDeleteMixin):
    pass


class ReleaseCreate(ReleaseBase):
    model_config = ConfigDict(extra="forbid")


@optional()
class ReleaseUpdate(ReleaseContentBase):
    model_config = ConfigDict(extra="forbid")


class ReleaseDelete(SoftDeleteMixin):
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
