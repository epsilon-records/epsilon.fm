# Local Dependencies
from src.core.common.crud import CRUDBase
from src.apps.system.tiers.models import Tier
from src.apps.system.tiers.schemas import (
    TierCreateInternal,
    TierUpdate,
    TierUpdateInternal,
    TierDelete,
)

# CRUD operations for the 'Tier' model
CRUDTier = CRUDBase[Tier, TierCreateInternal, TierUpdate, TierUpdateInternal, TierDelete]

# Create an instance of CRUDTier for the 'Tier' model
crud_tiers = CRUDTier(Tier)
