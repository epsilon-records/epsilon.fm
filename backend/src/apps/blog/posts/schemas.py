# Built-in Dependencies
from datetime import datetime

# Third-Party Dependencies
from pydantic import ConfigDict

# Local Dependencies
from src.apps.blog.posts.models import PostContentBase, PostMediaBase, PostUserBase
from src.core.common.models import UUIDMixin, TimestampMixin, SoftDeleteMixin
from src.core.utils.partial import optional


class PostBase(PostContentBase):
    pass


class Post(PostBase, PostMediaBase, PostUserBase, UUIDMixin, TimestampMixin, SoftDeleteMixin):
    pass


class PostRead(PostBase, PostMediaBase, PostUserBase, UUIDMixin, TimestampMixin):
    pass


class PostCreate(PostBase, PostMediaBase):
    model_config = ConfigDict(extra="forbid")


class PostCreateInternal(PostCreate, PostUserBase):
    pass


@optional()
class PostUpdate(PostContentBase, PostMediaBase):
    model_config = ConfigDict(extra="forbid")


class PostUpdateInternal(PostUpdate):
    updated_at: datetime


class PostDelete(SoftDeleteMixin):
    model_config = ConfigDict(extra="forbid")
