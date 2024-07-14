# Third-Party Dependencies
from sqlmodel import Field, text

# Local Dependencies
from src.core.common.models import TimestampMixin, UUIDMixin, Base


class TierInfoBase(Base):
    name: str = Field(
        min_length=2,
        max_length=25,
        nullable=False,
        unique=True,
        description="Tier name",
        schema_extra={"examples": ["Free"]},
    )


class TierRulesBase(Base):
    default: bool = Field(
        default=False,
        sa_column_kwargs={"server_default": text("false")},
        description="Indicates whether the tier is the default tier",
    )


class Tier(UUIDMixin, TierInfoBase, TierRulesBase, TimestampMixin, table=True):
    __tablename__ = "system_tier"
    __table_args__ = {"comment": "Tier information"}
