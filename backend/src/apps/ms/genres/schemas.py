# Built-in Dependencies
from datetime import datetime

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


class GenreRead(GenreBase, UUIDMixin, TimestampMixin):
    pass


class GenreCreate(GenreBase):
    model_config = ConfigDict(extra="forbid")


class GenreCreateInternal(GenreCreate):
    pass


@optional()
class GenreUpdate(GenreContentBase):
    model_config = ConfigDict(extra="forbid")


class GenreUpdateInternal(GenreUpdate):
    updated_at: datetime


class GenreDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
