# Local Dependencies
from src.core.common.crud import CRUDBase
from src.apps.system.rate_limits.models import RateLimit
from src.apps.system.rate_limits.schemas import (
    RateLimitCreateInternal,
    RateLimitUpdate,
    RateLimitUpdateInternal,
    RateLimitDelete,
)

# CRUD operations for RateLimit model
CRUDRateLimit = CRUDBase[
    RateLimit,
    RateLimitCreateInternal,
    RateLimitUpdate,
    RateLimitUpdateInternal,
    RateLimitDelete,
]

# Create an instance of CRUDRateLimit for the 'RateLimit' model
crud_rate_limits = CRUDRateLimit(RateLimit)
