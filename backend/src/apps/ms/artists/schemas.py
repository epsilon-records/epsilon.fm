# Built-in Dependencies
from datetime import datetime

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.ms.artists.models import (
    ArtistContentBase,
    ArtistMediaBase,
    ArtistUserBase,
)
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional


class ArtistBase(ArtistContentBase):
    """
    Base class for Artist models.

    Inherits from ArtistContentBase.
    """

    pass


class Artist(
    ArtistBase,
    ArtistMediaBase,
    ArtistUserBase,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
):
    """
    Comprehensive Artist model.

    Inherits from ArtistBase, ArtistMediaBase, ArtistUserBase, UUIDMixin, TimestampMixin, and SoftDeleteMixin.
    Represents a complete artist entity with all attributes and functionalities.
    """

    pass


class ArtistDB(ArtistBase, ArtistMediaBase, UUIDMixin, TimestampMixin):
    """
    Database representation of an Artist.

    Inherits from ArtistBase, ArtistMediaBase, UUIDMixin, and TimestampMixin.
    Used for database operations and storage.
    """

    pass


class ArtistRead(ArtistBase, ArtistMediaBase, UUIDMixin, TimestampMixin):
    """
    Represents an artist with read-only properties.

    Inherits from ArtistBase, ArtistMediaBase, UUIDMixin, and TimestampMixin.

    Attributes:
        slug (str): The slug of the artist.
        stage_name (str): The stage name of the artist.
        __tablename__ (str): The name of the database table associated with the artist.
        model_config (ConfigDict): The configuration dictionary for the artist model.
    """

    slug: str
    stage_name: str
    __tablename__ = None
    model_config = ConfigDict(from_attributes=True)


class ArtistCreate(ArtistBase, ArtistMediaBase):
    """
    Model for creating a new Artist.

    Inherits from ArtistBase and ArtistMediaBase.
    Used when creating a new artist entry.

    Attributes:
        model_config (ConfigDict): Configuration to forbid extra attributes.
    """

    model_config = ConfigDict(extra="forbid")


class ArtistCreateInternal(ArtistCreate, ArtistUserBase):
    """
    Internal model for creating a new Artist.

    Inherits from ArtistCreate and ArtistUserBase.
    Used internally for creating a new artist with user-related information.
    """

    pass


@optional()
class ArtistUpdate(ArtistContentBase, ArtistMediaBase):
    """
    Model for updating an existing Artist.

    Inherits from ArtistContentBase and ArtistMediaBase.
    Used when updating an existing artist entry.
    All fields are optional due to the @optional() decorator.

    Attributes:
        model_config (ConfigDict): Configuration to forbid extra attributes.
    """

    model_config = ConfigDict(extra="forbid")


class ArtistUpdateInternal(ArtistUpdate):
    """
    Internal model for updating an existing Artist.

    Inherits from ArtistUpdate.
    Used internally for updating an artist with additional metadata.

    Attributes:
        updated_at (datetime): The timestamp of the last update.
    """

    updated_at: datetime


class ArtistDelete(SoftDeleteMixin):
    """
    Model for soft-deleting an Artist.

    Inherits from SoftDeleteMixin.
    Used when performing a soft delete operation on an artist.

    Attributes:
        model_config (ConfigDict): Configuration to forbid extra attributes.
    """

    model_config = ConfigDict(extra="forbid")
