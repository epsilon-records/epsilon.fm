# Built-in Dependencies
from uuid import UUID

# Third-Party Dependencies
from sqlmodel import Field

# Local Dependencies
from src.core.common.models import TimestampMixin, UUIDMixin, Base


class RateLimitConfigBase(Base):
    path: str = Field(
        min_length=2,
        max_length=255,
        nullable=False,
        description="API path for rate limit",
        schema_extra={"examples": ["users"]},
    )
    limit: int = Field(
        ge=0,
        description="Number of requests allowed in the specified period",
        schema_extra={"examples": [5]},
    )
    period: int = Field(
        ge=0,
        description="Time period (in seconds) during which the limit applies",
        schema_extra={"examples": [60]},
    )


class RateLimitNameBase(Base):
    name: str = Field(
        min_length=2,
        max_length=100,
        nullable=False,
        unique=True,
        description="Rate limit name",
        schema_extra={"examples": ["users:5:60"]},
    )


class RateLimitTierBase(Base):
    tier_id: UUID = Field(
        description="Tier ID to which the rate limit is associated",
        foreign_key="system_tier.id",
        index=True,
    )


class RateLimit(
    UUIDMixin, RateLimitConfigBase, RateLimitNameBase, RateLimitTierBase, TimestampMixin, table=True
):
    __tablename__ = "system_rate_limit"
    __table_args__ = ({"comment": "Rate limit configuration"},)
