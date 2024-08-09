# Built-in Dependencies

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.ms.genres.models import GenreContentBase
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional


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
