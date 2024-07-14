# Built-in Dependencies
from uuid import UUID

# Third-Party Dependencies
from sqlmodel import Field, text

# Local Dependencies
from src.core.common.models import (
    SoftDeleteMixin,
    TimestampMixin,
    UUIDMixin,
    Base,
)


class UserPersonalInfoBase(Base):
    name: str = Field(
        min_length=2,
        max_length=100,
        nullable=False,
        description="User's full name",
        schema_extra={"examples": ["User Userson"]},
    )
    username: str = Field(
        min_length=2,
        max_length=20,
        unique=True,
        index=True,
        nullable=False,
        regex=r"^[a-z0-9]+$",
        description="User's username",
        schema_extra={"examples": ["userson"]},
    )
    email: str = Field(
        max_length=50,
        unique=True,
        index=True,
        nullable=False,
        regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        description="User's email address",
        schema_extra={"examples": ["user.userson@example.com"]},
    )  # Todo: Use EmailStr when it's supported by SQLModel (https://github.com/tiangolo/sqlmodel/pull/762)


class UserMediaBase(Base):
    profile_image_url: str = Field(
        default="https://www.imageurl.com/default_profile_image.jpg",
        description="URL of the user's profile image",
        schema_extra={"examples": ["https://www.imageurl.com/profile_image.jpg"]},
    )


class UserPermissionBase(Base):
    is_active: bool = Field(
        default=True,
        sa_column_kwargs={"server_default": text("true")},
        description="Indicates whether the user is active",
        schema_extra={"examples": [True]},
    )
    is_superuser: bool = Field(
        default=False,
        sa_column_kwargs={"server_default": text("false")},
        description="Indicates whether the user has superuser privileges",
    )


class UserSecurityBase(Base):
    hashed_password: str = Field(
        nullable=False, description="Hashed password for user authentication"
    )


class UserTierBase(Base):
    tier_id: UUID | None = Field(
        default=None,
        foreign_key="system_tier.id",
        index=True,
        description="ID of the tier to which the user belongs",
    )


class User(
    UUIDMixin,
    UserPersonalInfoBase,
    UserMediaBase,
    UserPermissionBase,
    UserSecurityBase,
    UserTierBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "admin_user"
    __table_args__ = ({"comment": "User account information"},)
