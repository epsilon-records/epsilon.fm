# Built-in Dependencies
from datetime import datetime

# Third-Party Dependencies
from pydantic import ConfigDict, field_validator

# Local Dependencies
from src.core.common.models import Base, UUIDMixin, TimestampMixin
from src.core.utils.rate_limit import sanitize_path
from src.core.utils.partial import optional
from src.apps.system.rate_limits.models import (
    RateLimitConfigBase,
    RateLimitNameBase,
    RateLimitTierBase,
)


class RateLimitBase(RateLimitConfigBase):
    @field_validator("path")
    def validate_and_sanitize_path(cls, v: str) -> str:
        return sanitize_path(v)


class RateLimit(TimestampMixin, RateLimitBase, RateLimitNameBase, RateLimitTierBase):
    pass


class RateLimitRead(UUIDMixin, RateLimitBase, RateLimitNameBase, RateLimitTierBase):
    pass


class RateLimitCreate(RateLimitBase, RateLimitNameBase):
    model_config = ConfigDict(extra="forbid")


class RateLimitCreateInternal(RateLimitCreate, RateLimitTierBase):
    pass


@optional()
class RateLimitUpdate(RateLimitBase, RateLimitNameBase):
    model_config = ConfigDict(extra="forbid")


class RateLimitUpdateInternal(RateLimitUpdate):
    updated_at: datetime


class RateLimitDelete(Base):
    pass
