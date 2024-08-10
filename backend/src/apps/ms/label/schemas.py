# Built-in Dependencies

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.ms.label.models import LabelContentBase
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional


class LabelBase(LabelContentBase):
    pass


class Label(LabelBase, UUIDMixin, TimestampMixin, SoftDeleteMixin):
    pass


class LabelCreate(LabelBase):
    model_config = ConfigDict(extra="forbid")


@optional()
class LabelUpdate(LabelContentBase):
    model_config = ConfigDict(extra="forbid")


class LabelDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
