# Built-in Dependencies
from uuid import UUID
from datetime import date
from typing import Optional

# Third-Party Dependencies
from sqlmodel import Field

# Local Dependencies
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, Base


class ArtistContentBase(Base):
    id: Optional[int] = Field(default=None, primary_key=True)
    org_id: str = Field(max_length=255, unique=True)
    slug: str = Field(max_length=255)
    email: str = Field(max_length=255)
    biography: str = Field(
        max_length=1000,
        description="Artist Biography",
        schema_extra={"examples": ["This is the biography of an example artist."]}
    )
    spotify_artist_link: Optional[str] = Field(
        default=None, 
        max_length=255,
        description="Artist Spotify URI",
        schema_extra={"examples": ["https://open.spotify.com/artist/123456789"]}
    )
    youtube_channel_link: Optional[str] = Field(
        default=None, 
        max_length=255,
        description="Artist YouTube URL",
        schema_extra={"examples": ["https://www.youtube.com/channel/exampleartist"]}
    )
    instagram_profile_link: Optional[str] = Field(
        default=None, 
        max_length=255,
        description="Artist Instagram URL",
        schema_extra={"examples": ["https://www.instagram.com/exampleartist/"]}
    )
    facebook_profile_link: Optional[str] = Field(
        default=None, 
        max_length=255,
        description="Artist Facebook URL",
        schema_extra={"examples": ["https://www.facebook.com/exampleartist/"]}
    )
    x_profile_link: Optional[str] = Field(
        default=None, 
        max_length=255,
        description="Artist X URL",
        schema_extra={"examples": ["https://www.x.com/exampleartist"]}
    )
    tiktok_profile_link: Optional[str] = Field(
        default=None, 
        max_length=255,
        description="Artist TikTok URL",
        schema_extra={"examples": ["https://www.tiktok.com/@exampleartist"]}
    )
    soundcloud_profile_link: Optional[str] = Field(
        default=None, 
        max_length=255,
        description="Artist SoundCloud URL",
        schema_extra={"examples": ["https://soundcloud.com/exampleartist"]}
    )
    songkick_profile_link: Optional[str] = Field(
        default=None, 
        max_length=255,
        description="Artist SongKick URL",
        schema_extra={"examples": ["https://www.songkick.com/artists/exampleartist"]}
    )
    bandsintown_profile_link: Optional[str] = Field(
        default=None, 
        max_length=255,
        description="Artist BandsInTown URL",
        schema_extra={"examples": ["https://www.bandsintown.com/artists/exampleartist"]}
    )


class ArtistMediaBase(Base):
    media_url: str | None = Field(
        max_length=255,
        nullable=True,
        default=None,
        regex=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$",
        description="URL of the media associated with the post",
        schema_extra={"examples": ["https://www.imageurl.com/example.jpg"]},
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
