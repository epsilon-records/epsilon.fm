# Local Dependencies
from src.apps.auth.schemas import (
    TokenBlacklistCreate,
    TokenBlacklistUpdate,
)
from src.apps.auth.models import TokenBlacklist
from src.core.common.crud import CRUDBase

# Define a CRUD (Create, Read, Update, Delete) interface for the TokenBlacklist model
CRUDTokenBlacklist = CRUDBase[
    TokenBlacklist,
    TokenBlacklistCreate,
    TokenBlacklistUpdate,
    TokenBlacklistUpdate,
    None,
]

# Create an instance of the CRUDTokenBlacklist with the TokenBlacklist model
crud_token_blacklist = CRUDTokenBlacklist(TokenBlacklist)
