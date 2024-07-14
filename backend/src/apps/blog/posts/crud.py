# Local Dependencies
from src.core.common.crud import CRUDBase
from src.apps.blog.posts.models import Post
from src.apps.blog.posts.schemas import (
    PostCreateInternal,
    PostUpdate,
    PostUpdateInternal,
    PostDelete,
)

# Define CRUD operations for the 'Post' model
CRUDPost = CRUDBase[Post, PostCreateInternal, PostUpdate, PostUpdateInternal, PostDelete]

# Create an instance of CRUDPost for the 'Post' model
crud_posts = CRUDPost(Post)
