# Third-Party Dependencies
from pydantic import BaseModel, ConfigDict

# Local Dependencies
from src.apps.auth.models import TokenBlacklistBase
from src.core.utils.partial import optional


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username_or_email: str


class TokenBlacklistCreate(TokenBlacklistBase):
    pass


# All these fields are optional
@optional()
class TokenBlacklistUpdate(TokenBlacklistBase):
    model_config = ConfigDict(extra="forbid")
