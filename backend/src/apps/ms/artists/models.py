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
        default="",
        max_length=255,
        nullable=False,
        description="Artist Spotify URI",
        regex=r"^(https?:\/\/)?(www\.)?open\.spotify\.com\/artist\/[^\s]+$",
    )
    youtube_channel_link: Optional[str] = Field(
        default="",
        max_length=255,
        nullable=False,
        description="Artist YouTube URL",
        regex=r"^(https?:\/\/)?(www\.)?youtube\.com\/(channel\/|user\/|c\/)?[^\s]+$",
    )
    instagram_profile_link: Optional[str] = Field(
        default="",
        max_length=255,
        nullable=False,
        description="Artist Instagram URL",
        regex=r"^(https?:\/\/)?(www\.)?instagram\.com\/[^\s]+$",
    )
    facebook_profile_link: Optional[str] = Field(
        default="",
        max_length=255,
        nullable=False,
        description="Artist Facebook URL",
        regex=r"^(https?:\/\/)?(www\.)?facebook\.com\/[^\s]+$",
    )
    x_profile_link: Optional[str] = Field(
        default="",
        max_length=255,
        nullable=False,
        description="Artist X URL",
        regex=r"^(https?:\/\/)?(www\.)?twitter\.com\/[^\s]+$",
    )
    tiktok_profile_link: Optional[str] = Field(
        default="",
        max_length=255,
        nullable=False,
        description="Artist TikTok URL",
        regex=r"^(https?:\/\/)?(www\.)?tiktok\.com\/@[^\s]+$",
    )
    soundcloud_profile_link: Optional[str] = Field(
        default="",
        max_length=255,
        nullable=False,
        description="Artist SoundCloud URL",
        regex=r"^(https?:\/\/)?(www\.)?soundcloud\.com\/[^\s]+$",
    )
    songkick_profile_link: Optional[str] = Field(
        default="",
        max_length=255,
        nullable=False,
        description="Artist SongKick URL",
        regex=r"^(https?:\/\/)?(www\.)?songkick\.com\/artists\/[^\s]+$",
    )
    bandsintown_profile_link: Optional[str] = Field(
        default="",
        max_length=255,
        nullable=False,
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
