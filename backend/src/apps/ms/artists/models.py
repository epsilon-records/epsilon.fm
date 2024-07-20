# Built-in Dependencies
from uuid import UUID
from typing import Optional

# Third-Party Dependencies
from sqlmodel import Field

# Local Dependencies
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, Base


class ArtistContentBase(Base):
    org_id: str = Field(max_length=255, unique=True)
    email: str = Field(max_length=255)
    biography: str = Field(
        max_length=1000,
        description="Artist Biography",
    )
    spotify_artist_link: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Artist Spotify URI",
    )
    youtube_channel_link: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Artist YouTube URL",
    )
    instagram_profile_link: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Artist Instagram URL",
    )
    facebook_profile_link: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Artist Facebook URL",
    )
    x_profile_link: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Artist X URL",
    )
    tiktok_profile_link: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Artist TikTok URL",
    )
    soundcloud_profile_link: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Artist SoundCloud URL",
    )
    songkick_profile_link: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Artist SongKick URL",
    )
    bandsintown_profile_link: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Artist BandsInTown URL",
    )


class ArtistMediaBase(Base):
    media_url: str | None = Field(
        max_length=255,
        nullable=True,
        default=None,
        regex=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$",
        description="URL of the media associated with the post",
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
    __tablename__ = "ms_artist"
    __table_args__ = ({"comment": "Management System artist information"},)
