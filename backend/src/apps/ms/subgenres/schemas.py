# Built-in Dependencies
from datetime import datetime

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.ms.subgenres.models import (
    SubgenreContentBase,
    SubgenreMediaBase,
    SubgenreUserBase,
)
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional


class SubgenreBase(SubgenreContentBase):
    pass


class Subgenre(
    SubgenreBase,
    SubgenreMediaBase,
    SubgenreUserBase,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
):
    pass


class SubgenreRead(
    SubgenreBase, SubgenreMediaBase, SubgenreUserBase, UUIDMixin, TimestampMixin
):
    pass


class SubgenreCreate(SubgenreBase, SubgenreMediaBase):
    model_config = ConfigDict(extra="forbid")


class SubgenreCreateInternal(SubgenreCreate, SubgenreUserBase):
    pass


@optional()
class SubgenreUpdate(SubgenreContentBase, SubgenreMediaBase):
    model_config = ConfigDict(extra="forbid")


class SubgenreUpdateInternal(SubgenreUpdate):
    updated_at: datetime


class SubgenreDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
