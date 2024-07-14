# Built-in Dependencies
from uuid import UUID
from datetime import date

# Third-Party Dependencies
from sqlmodel import Field

# Local Dependencies
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, Base


class ArtistContentBase(Base):
    artist_stage_name: str = Field(
        max_length=255,
        nullable=False,
        description="Artist Stage Name",
        schema_extra={"examples": ["The Beatles"]},
    )
    legal_first_name: str = Field(
        max_length=255,
        nullable=False,
        description="Artist Legal First Name",
        schema_extra={"examples": ["John"]},
    )
    legal_last_name: str = Field(
        max_length=255,
        nullable=False,
        description="Artist Legal Last Name",
        schema_extra={"examples": ["Lennon"]},
    )
    birthdate: date = Field(
        description="Artist Birthdate",
        schema_extra={"examples": ["1940-10-09"]},
    )
    phone: str = Field(
        max_length=255,
        nullable=True,
        description="Artist Phone Number",
        schema_extra={"examples": ["+1 (555) 555-5555"]},
    )
    birth_location: str = Field(
        max_length=255,
        nullable=True,
        description="Artist Birth Location",
        schema_extra={"examples": ["New York, NY"]},
    )
    current_location: str = Field(
        max_length=255,
        nullable=True,
        description="Artist Current Location",
        schema_extra={"examples": ["Los Angeles, CA"]},
    )
    artist_biography: str = Field(
        max_length=1500,
        nullable=True,
        description="Artist Biography",
        schema_extra={"examples": ["This is the biography of an example artist."]},
    )
    artist_website: str = Field(
        max_length=255,
        nullable=True,
        description="Artist Website",
        schema_extra={"examples": ["https://www.exampleartist.com/"]},
    )
    spotify_uri: str = Field(
        max_length=255,
        nullable=True,
        description="Artist Spotify URI",
        schema_extra={"examples": ["https://open.spotify.com/artist/123456789"]},
    )
    apple_music_uri: str = Field(
        max_length=255,
        nullable=True,
        description="Artist Apple Music URI",
        schema_extra={"examples": ["https://music.apple.com/us/artist/exampleartist/123456789"]},
    )
    youtube_url: str = Field(
        max_length=255,
        nullable=True,
        description="Artist YouTube URL",
        schema_extra={"examples": ["https://www.youtube.com/channel/exampleartist"]},
    )
    instagram_url: str = Field(
        max_length=255,
        nullable=True,
        description="Artist Instagram URL",
        schema_extra={"examples": ["https://www.instagram.com/exampleartist/"]},
    )
    facebook_url: str = Field(
        max_length=255,
        nullable=True,
        description="Artist Facebook URL",
        schema_extra={"examples": ["https://www.facebook.com/exampleartist/"]},
    )
    x_url: str = Field(
        max_length=255,
        nullable=True,
        description="Artist X URL",
        schema_extra={"examples": ["https://www.x.com/exampleartist"]},
    )
    tiktok_url: str = Field(
        max_length=255,
        nullable=True,
        description="Artist TikTok URL",
        schema_extra={"examples": ["https://www.tiktok.com/@exampleartist"]},
    )
    soundcloud_url: str = Field(
        max_length=255,
        nullable=True,
        description="Artist SoundCloud URL",
        schema_extra={"examples": ["https://soundcloud.com/exampleartist"]},
    )
    songkick_url: str = Field(
        max_length=255,
        nullable=True,
        description="Artist SongKick URL",
        schema_extra={"examples": ["https://www.songkick.com/artists/exampleartist"]},
    )
    bandsintown_url: str = Field(
        max_length=255,
        nullable=True,
        description="Artist BandsInTown URL",
        schema_extra={"examples": ["https://www.bandsintown.com/artists/exampleartist"]},
    )
    how_did_you_hear_about_us: str = Field(
        max_length=255,
        nullable=True,
        description="How did you hear about us?",
    )
    anr_referral: str = Field(
        max_length=255,
        nullable=True,
        description="A&R Referral",
    )


class ArtistMediaBase(Base):
    media_url: str | None = Field(
        max_length=255,
        nullable=True,
        default=None,
        regex=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$",
        description="URL of the media associated with the post",
        schema_extra={"examples": ["https://www.imageurl.com/example_post.jpg"]},
    )


class ArtistUserBase(Base):
    user_id: UUID = Field(
        description="User ID associated with the artist",
        foreign_key="admin_user.id",
        index=True,
    )


class Artist(
    UUIDMixin,
    ArtistContentBase,
    ArtistUserBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "epsilon_artist"
    __table_args__ = ({"comment": "Epsilon artist information"},)
