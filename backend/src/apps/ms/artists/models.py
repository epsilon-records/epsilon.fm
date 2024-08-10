# Built-in Dependencies
from uuid import UUID
from typing import Optional

# Third-Party Dependencies
from sqlmodel import Field

# Local Dependencies
from src.core.common.models import (
    SoftDeleteMixin,
    TimestampMixin,
    UUIDMixin,
    OrgMixin,
    Base,
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
