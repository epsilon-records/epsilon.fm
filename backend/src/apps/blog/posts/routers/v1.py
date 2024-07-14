# Built-in Dependencies
from typing import Annotated, Dict
from uuid import UUID

# Third-Party Dependencies
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Request, Depends
import fastapi

# Local Dependencies
from src.core.api.dependencies import get_current_user, get_current_superuser
from src.apps.admin.users.schemas import UserRead
from src.apps.admin.users.crud import crud_users
from src.apps.blog.posts.crud import crud_posts
from src.core.db.session import async_get_db
from src.core.utils.cache import cache
from src.core.exceptions.http_exceptions import (
    NotFoundException,
    ForbiddenException,
)
from src.apps.blog.posts.schemas import (
    Post,
    PostCreate,
    PostUpdate,
    PostRead,
    PostCreateInternal,
)
from src.core.utils.paginated import (
    PaginatedListResponse,
    paginated_response,
    compute_offset,
)

# TODO: Improvment the cache strategy on composite routes. Eg: '/blog/posts/{post_id}/user/{user_id}' is not good.

router = fastapi.APIRouter(tags=["Blog - Posts"])


@router.post("/blog/posts/user/{user_id}", response_model=PostRead, status_code=201)
async def write_post(
    request: Request,
    user_id: UUID,
    post: PostCreate,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> PostRead:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    if current_user["id"] != db_user["id"]:
        raise ForbiddenException(detail="You are not allowed to create a post for this user")

    # Prepare the post data
    post_internal_dict = post.model_dump()
    post_internal_dict["user_id"] = current_user["id"]

    post_internal = PostCreateInternal(**post_internal_dict)
    return await crud_posts.create(db=db, object=post_internal)


@router.get("/blog/posts/user/{user_id}", response_model=PaginatedListResponse[PostRead])
@cache(
    key_prefix="blog:posts:user:{user_id}:page_{page}:items_per_page:{items_per_page}",
    resource_id_name="user_id",
    expiration=60,
)
async def read_posts(
    request: Request,
    user_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
    page: int = 1,
    items_per_page: int = 10,
) -> dict:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if not db_user:
        raise NotFoundException(detail="User not found")

    posts_data = await crud_posts.get_multi(
        db=db,
        offset=compute_offset(page, items_per_page),
        limit=items_per_page,
        schema_to_select=PostRead,
        user_id=db_user["id"],
        is_deleted=False,
    )

    return paginated_response(crud_data=posts_data, page=page, items_per_page=items_per_page)


@router.get("/blog/posts/{post_id}/user/{user_id}", response_model=PostRead)
@cache(key_prefix="blog:posts:user:{user_id}:post_cache", resource_id_name="post_id")
async def read_post(
    request: Request,
    user_id: UUID,
    post_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> dict:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    db_post = await crud_posts.get(
        db=db,
        schema_to_select=PostRead,
        id=post_id,
        user_id=db_user["id"],
        is_deleted=False,
    )
    if db_post is None:
        raise NotFoundException(detail="Post not found")

    return db_post


@router.patch("/blog/posts/{post_id}/user/{user_id}")
@cache(
    "blog:posts:user:{user_id}:post_cache",
    resource_id_name="post_id",
    pattern_to_invalidate_extra=["blog:posts:user:{user_id}:*"],
)
async def patch_post(
    request: Request,
    user_id: UUID,
    post_id: UUID,
    values: PostUpdate,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    if str(db_user["id"]) != str(current_user["id"]):
        raise ForbiddenException(detail="You are not allowed to update this post")

    db_post = await crud_posts.get(db=db, schema_to_select=PostRead, id=post_id, is_deleted=False)
    if db_post is None:
        raise NotFoundException(detail="Post not found")

    await crud_posts.update(db=db, object=values, id=post_id)
    return {"message": "Post updated"}


@router.delete("/blog/posts/{post_id}/user/{user_id}")
@cache(
    "blog:posts:user:{user_id}:post_cache",
    resource_id_name="post_id",
    pattern_to_invalidate_extra=["blog:posts:user:{user_id}:*"],
)
async def erase_post(
    request: Request,
    user_id: UUID,
    post_id: UUID,
    current_user: Annotated[UserRead, Depends(get_current_user)],
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    if not current_user["is_superuser"] and str(current_user["id"]) != str(db_user["id"]):
        raise ForbiddenException(detail="You are not allowed to delete this post")

    db_post = await crud_posts.get(db=db, schema_to_select=Post, id=post_id, is_deleted=False)
    if db_post is None or db_post["is_deleted"]:
        if current_user["is_superuser"]:
            raise NotFoundException(detail="Post already deleted (soft delete).")
        raise NotFoundException(detail="Post not found")

    await crud_posts.delete(db=db, db_row=db_post, id=post_id)

    return {"message": "Post deleted"}


@router.delete(
    "/blog/posts/{post_id}/user/{user_id}/db",
    dependencies=[Depends(get_current_superuser)],
)
@cache(
    "blog:posts:user:{user_id}:post_cache",
    resource_id_name="post_id",
    pattern_to_invalidate_extra=["blog:posts:user:{user_id}:*"],
)
async def erase_db_post(
    request: Request,
    user_id: UUID,
    post_id: UUID,
    db: Annotated[AsyncSession, Depends(async_get_db)],
) -> Dict[str, str]:
    db_user = await crud_users.get(db=db, schema_to_select=UserRead, id=user_id, is_deleted=False)
    if db_user is None:
        raise NotFoundException(detail="User not found")

    db_post = await crud_posts.get(db=db, schema_to_select=PostRead, id=post_id)
    if db_post is None:
        raise NotFoundException(detail="Post not found")

    await crud_posts.db_delete(db=db, id=post_id)
    return {"message": "Post deleted from the database"}
