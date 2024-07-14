# Built-in Dependencies
from datetime import datetime
from uuid import UUID

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.system.tiers.models import Base, TierInfoBase, TierRulesBase
from src.core.common.models import TimestampMixin
from src.core.utils.partial import optional


class Tier(TimestampMixin, TierInfoBase, TierRulesBase):
    pass


class TierRead(TierInfoBase, TierRulesBase):
    id: UUID
    created_at: datetime


class TierCreate(TierInfoBase):
    model_config = ConfigDict(extra="forbid")


class TierCreateInternal(TierCreate):
    pass


@optional()
class TierUpdate(TierInfoBase):
    model_config = ConfigDict(extra="forbid")


class TierUpdateInternal(TierUpdate):
    updated_at: datetime


class TierDelete(Base):
    pass
