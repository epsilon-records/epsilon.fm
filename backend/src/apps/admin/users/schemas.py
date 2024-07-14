# Built-in Dependencies
from typing import Annotated
from datetime import datetime

# Third-Party Dependencies
from pydantic import Field, ConfigDict

# Local Dependencies
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional
from src.apps.admin.users.models import (
    UserPersonalInfoBase,
    UserMediaBase,
    UserTierBase,
    UserPermissionBase,
    UserSecurityBase,
)


class UserBase(UserPersonalInfoBase):
    pass


class User(
    UserBase,
    UserMediaBase,
    UserTierBase,
    UserPermissionBase,
    UserSecurityBase,
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
):
    pass


class UserRead(UserBase, UserMediaBase, UserTierBase, UUIDMixin):
    pass


class UserCreate(UserBase):
    model_config = ConfigDict(extra="forbid")

    password: Annotated[
        str,
        Field(
            pattern=r"^.{8,}|[0-9]+|[A-Z]+|[a-z]+|[^a-zA-Z0-9]+$",
            examples=["Str1ngst!"],
        ),
    ]


class UserCreateInternal(UserBase, UserSecurityBase, UserTierBase):
    pass


@optional()
class UserUpdate(UserBase, UserMediaBase):
    model_config = ConfigDict(extra="forbid")


class UserUpdateInternal(UserUpdate):
    updated_at: datetime


class UserTierUpdate(UserTierBase):
    model_config = ConfigDict(extra="forbid")


class UserDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
