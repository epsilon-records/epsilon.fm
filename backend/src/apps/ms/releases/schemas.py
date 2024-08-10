# Built-in Dependencies

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.ms.releases.models import ReleaseContentBase
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional


class ReleaseBase(ReleaseContentBase):
    pass


class Release(ReleaseBase, UUIDMixin, TimestampMixin, SoftDeleteMixin):
    pass


class ReleaseCreate(ReleaseBase):
    model_config = ConfigDict(extra="forbid")


@optional()
class ReleaseUpdate(ReleaseContentBase):
    model_config = ConfigDict(extra="forbid")


class ReleaseDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
