# Built-in Dependencies
from uuid import UUID
from datetime import date

# Third-Party Dependencies
from sqlmodel import Field, Relationship

# Local Dependencies
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, Base
from src.apps.ms.genres.models import Genre
from src.apps.ms.subgenres.models import Subgenre


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
