# Local Dependencies
from src.core.common.crud import CRUDBase
from src.apps.admin.users.models import User
from src.apps.admin.users.schemas import (
    UserCreateInternal,
    UserUpdate,
    UserUpdateInternal,
    UserDelete,
)

# CRUD operations for the 'User' model
CRUDUser = CRUDBase[User, UserCreateInternal, UserUpdate, UserUpdateInternal, UserDelete]

# Create an instance of CRUDUser for the 'User' model
crud_users = CRUDUser(User)
