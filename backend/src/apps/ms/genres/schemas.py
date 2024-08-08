# Built-in Dependencies
from datetime import datetime

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.ms.genres.models import GenreContentBase, GenreMediaBase, GenreUserBase
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional


class GenreBase(GenreContentBase):
    pass


class Genre(
    GenreBase, GenreMediaBase, GenreUserBase, UUIDMixin, TimestampMixin, SoftDeleteMixin
):
    pass


class GenreRead(GenreBase, GenreMediaBase, GenreUserBase, UUIDMixin, TimestampMixin):
    pass


class GenreCreate(GenreBase, GenreMediaBase):
    model_config = ConfigDict(extra="forbid")


class GenreCreateInternal(GenreCreate, GenreUserBase):
    pass


@optional()
class GenreUpdate(GenreContentBase, GenreMediaBase):
    model_config = ConfigDict(extra="forbid")


class GenreUpdateInternal(GenreUpdate):
    updated_at: datetime


class GenreDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
