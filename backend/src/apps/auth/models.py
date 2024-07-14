# Built-in Dependencies
from datetime import datetime

# Third-Party Dependencies
from sqlmodel import Field

# Local Dependencies
from src.core.common.models import TimestampMixin, UUIDMixin, Base


class TokenBlacklistBase(Base):
    token: str = Field(
        index=True,
        nullable=False,
        default=None,
        description="Token value for authentication",
    )
    expires_at: datetime = Field(
        nullable=False,
        default=None,
        description="Timestamp indicating the expiration date and time of the token",
    )


class TokenBlacklist(UUIDMixin, TokenBlacklistBase, TimestampMixin, table=True):
    __tablename__ = "system_token_blacklist"
    __table_args__ = {"comment": "Token blacklist for authentication"}
