# Built-in Dependencies
import asyncio

# Third-Party Dependencies
from sqlmodel import select

# Local Dependencies
from src.core.db.session import AsyncSession, local_session
from src.apps.blog.posts.models import Post
from src.apps.admin.users.models import User
from src.core.config import settings


async def create_first_post(session: AsyncSession) -> None:
    # First post data
    test_post = {
        "title": "This is my first post",
        "text": "This is the content of my first post.",
        "media_url": "https://www.imageurl.com/first_post.jpg",
    }

    # Checking if post already exists
    query = select(Post).where(
        Post.title == test_post["title"],
        Post.text == test_post["text"],
        Post.media_url == test_post["media_url"],
    )
    result = await session.exec(query)
    post = result.one_or_none()

    # Creating post if it doesn't exist
    if post is None:
        # Getting admin user as post author
        query = select(User).where(User.username == settings.ADMIN_USERNAME)
        result = await session.exec(query)
        user = result.one_or_none()

        if user is None:
            raise Exception("Admin user not found")

        # Creating first post
        session.add(
            Post(
                title=test_post["title"],
                text=test_post["text"],
                media_url=test_post["media_url"],
                user_id=user.id,
            )
        )

        await session.commit()


async def main():
    async with local_session() as session:
        await create_first_post(session)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
