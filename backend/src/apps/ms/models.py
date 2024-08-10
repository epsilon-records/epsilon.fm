# Built-in Dependencies
from uuid import UUID
from datetime import date
from typing import Optional

# Third-Party Dependencies
from sqlmodel import Field, Relationship

# Local Dependencies
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, Base
from src.core.common.models import (
    OrgMixin,
)


class ArtistProfileBase(Base):
    email: str = Field(max_length=255)
    biography: str = Field(
        max_length=1000,
        description="Artist Biography",
    )
    apple_artist_link: str = Field(
        default="",
        max_length=255,
        description="Artist Apple URL",
        regex=r"^(https?):\/\/music.apple.com\/artist\/[^\s]+$",
    )
    beatport_artist_link: str = Field(
        default="",
        max_length=255,
        description="Artist Beatport URL",
        regex=r"^(https?):\/\/www.beatport.com\/artist\/[^\s]+$",
    )
    deezer_artist_link: str = Field(
        default="",
        max_length=255,
        description="Artist Deezer URL",
        regex=r"^(https?):\/\/deezer.com\/artist\/[^\s]+$",
    )
    tidal_artist_link: str = Field(
        default="",
        max_length=255,
        description="Artist Tidal URL",
        regex=r"^(https?):\/\/tidal.com\/browse\/artist\/[^\s]+$",
    )
    pandora_artist_link: str = Field(
        default="",
        max_length=255,
        description="Artist Pandora URL",
        regex=r"^(https?):\/\/www.pandora.com\/artist\/[^\s]+$",
    )
    shazam_artist_link: str = Field(
        default="",
        max_length=255,
        description="Artist Shazam URL",
        regex=r"^(https?):\/\/www.shazam.com\/artist\/[^\s]+$",
    )
    spotify_artist_link: str = Field(
        default="",
        max_length=255,
        description="Artist Spotify URI",
        regex=r"^(https?:\/\/)?(www\.)?open\.spotify\.com\/artist\/[^\s]+$",
    )
    youtube_channel_link: str = Field(
        default="",
        max_length=255,
        description="Artist YouTube URL",
        regex=r"^(https?:\/\/)?(www\.)?youtube\.com\/(channel\/|user\/|c\/)?[^\s]+$",
    )
    instagram_profile_link: str = Field(
        default="",
        max_length=255,
        description="Artist Instagram URL",
        regex=r"^(https?:\/\/)?(www\.)?instagram\.com\/[^\s]+$",
    )
    facebook_profile_link: str = Field(
        default="",
        max_length=255,
        description="Artist Facebook URL",
        regex=r"^(https?:\/\/)?(www\.)?facebook\.com\/[^\s]+$",
    )
    x_profile_link: str = Field(
        default="",
        max_length=255,
        description="Artist X URL",
        regex=r"^(https?:\/\/)?(www\.)?twitter\.com\/[^\s]+$",
    )
    tiktok_profile_link: str = Field(
        default="",
        max_length=255,
        description="Artist TikTok URL",
        regex=r"^(https?:\/\/)?(www\.)?tiktok\.com\/@[^\s]+$",
    )
    soundcloud_profile_link: str = Field(
        default="",
        max_length=255,
        description="Artist SoundCloud URL",
        regex=r"^(https?:\/\/)?(www\.)?soundcloud\.com\/[^\s]+$",
    )
    songkick_profile_link: str = Field(
        default="",
        max_length=255,
        description="Artist SongKick URL",
        regex=r"^(https?:\/\/)?(www\.)?songkick\.com\/artists\/[^\s]+$",
    )
    bandsintown_profile_link: str = Field(
        default="",
        max_length=255,
        description="Artist BandsInTown URL",
        regex=r"^(https?:\/\/)?(www\.)?bandsintown\.com\/a\/[^\s]+$",
    )


class ArtistMediaBase(Base):
    media_url: Optional[str] = Field(
        max_length=255,
        nullable=True,
        default=None,
        regex=r"^(https?):\/\/[^\s\/$.?#].[^\s]*\.(jpg|jpeg|png|gif)$",
        description="URL of the media associated with the post",
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
    OrgMixin,
    ArtistProfileBase,
    ArtistAnalyticsBase,
    ArtistMediaBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_artist"
    __table_args__ = ({"comment": "Management System artist information"},)


class GenreContentBase(Base):
    genre_name: str = Field(
        max_length=255,
        nullable=False,
        description="Genre Name",
        schema_extra={"examples": ["Electronic"]},
    )


class Genre(
    UUIDMixin,
    GenreContentBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_genre"
    __table_args__ = ({"comment": "Management System genre information"},)


class SubgenreContentBase(Base):
    subgenre_name: str = Field(
        max_length=255,
        nullable=False,
        description="Subgenre Name",
        schema_extra={"examples": ["Minimal Techno"]},
    )


class Subgenre(
    UUIDMixin,
    SubgenreContentBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_subgenre"
    __table_args__ = ({"comment": "Management System subgenre information"},)


class TrackContentBase(Base):
    isrc: str = Field(
        max_length=255,
        nullable=False,
        description="Track ISRC",
        schema_extra={"examples": ["QZWDD2467025"]},
    )
    iswc: str = Field(
        max_length=255,
        nullable=False,
        description="Track ISWC",
    )
    track_name: str = Field(
        max_length=255,
        nullable=False,
        description="Track Name",
        schema_extra={"examples": ["Here Comes the Sun"]},
    )
    track_version: str = Field(
        max_length=255,
        nullable=False,
        description="Track Version",
        schema_extra={"examples": ["Remixes"]},
    )
    birthdate: date = Field(
        description="Track Birthdate",
        schema_extra={"examples": ["1940-10-09"]},
    )
    phone: str = Field(
        max_length=255,
        nullable=True,
        description="Track Phone Number",
        schema_extra={"examples": ["+1 (555) 555-5555"]},
    )
    birth_location: str = Field(
        max_length=255,
        nullable=True,
        description="Track Birth Location",
        schema_extra={"examples": ["New York, NY"]},
    )
    current_location: str = Field(
        max_length=255,
        nullable=True,
        description="Track Current Location",
        schema_extra={"examples": ["Los Angeles, CA"]},
    )
    track_biography: str = Field(
        max_length=1500,
        nullable=True,
        description="Track Biography",
        schema_extra={"examples": ["This is the biography of an example track."]},
    )
    track_website: str = Field(
        max_length=255,
        nullable=True,
        description="Track Website",
        schema_extra={"examples": ["https://www.exampletrack.com/"]},
    )
    spotify_uri: str = Field(
        max_length=255,
        nullable=True,
        description="Track Spotify URI",
        schema_extra={"examples": ["https://open.spotify.com/track/123456789"]},
    )
    apple_music_uri: str = Field(
        max_length=255,
        nullable=True,
        description="Track Apple Music URI",
        schema_extra={
            "examples": ["https://music.apple.com/us/track/exampletrack/123456789"]
        },
    )
    youtube_url: str = Field(
        max_length=255,
        nullable=True,
        description="Track YouTube URL",
        schema_extra={"examples": ["https://www.youtube.com/channel/exampletrack"]},
    )
    primary_genre_id: UUID = Field(
        nullable=False,
        foreign_key="ms_genre.id",
        description="Primary Genre ID",
    )
    primary_subgenre_id: UUID = Field(
        nullable=False,
        foreign_key="ms_subgenre.id",
        description="Primary Subgenre ID",
    )


class TrackMediaBase(Base):
    media_url: str | None = Field(
        max_length=255,
        nullable=True,
        default=None,
        regex=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$",
        description="URL of the media associated with the post",
        schema_extra={"examples": ["https://www.imageurl.com/example_post.jpg"]},
    )


class TrackUserBase(Base):
    user_id: UUID = Field(
        description="User ID associated with the track",
        foreign_key="admin_user.id",
        index=True,
    )


class Track(
    UUIDMixin,
    TrackContentBase,
    TrackUserBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_track"
    __table_args__ = ({"comment": "Management System track information"},)

    primary_genre: "Genre" = Relationship(
        sa_relationship_kwargs={"primaryjoin": "Track.primary_genre_id == Genre.id"}
    )
    primary_subgenre: "Subgenre" = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Track.primary_subgenre_id == Subgenre.id"
        }
    )


class ReleaseContentBase(Base):
    release_name: str = Field(
        max_length=255,
        nullable=False,
        description="Release Name",
        schema_extra={"examples": ["Electronic"]},
    )


class Release(
    UUIDMixin,
    ReleaseContentBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_release"
    __table_args__ = ({"comment": "Management System release information"},)


class AlbumContentBase(Base):
    album_name: str = Field(
        max_length=255,
        nullable=False,
        description="Album Name",
        schema_extra={"examples": ["Electronic"]},
    )


class Album(
    UUIDMixin,
    AlbumContentBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_album"
    __table_args__ = ({"comment": "Management System album information"},)
