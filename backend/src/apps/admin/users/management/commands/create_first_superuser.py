# Built-in Dependencies
import asyncio

# Third-Party Dependencies
from sqlmodel import select

# Local Dependencies
from src.core.db.session import AsyncSession, local_session
from src.core.security import get_password_hash
from src.apps.admin.users.models import User
from src.apps.system.tiers.models import Tier
from src.core.config import settings


async def create_first_user(session: AsyncSession) -> None:
    # First user/admin data
    name = settings.ADMIN_NAME
    email = settings.ADMIN_EMAIL
    username = settings.ADMIN_USERNAME
    hashed_password = get_password_hash(settings.ADMIN_PASSWORD)

    # Checking if user already exists
    query = select(User).filter_by(email=email)
    result = await session.exec(query)
    user = result.one_or_none()

    # Creating admin user if it doesn't exist
    if user is None:
        # Getting default tier to assign to first user/admin
        query = select(Tier).where(Tier.name == settings.TIER_NAME_DEFAULT)
        result = await session.exec(query)
        tier = result.one_or_none()

        if tier is None:
            raise Exception("Default tier not found")

        # Validating user data
        # See: https://github.com/tiangolo/sqlmodel/issues/52#issuecomment-1311987732
        db_user = User.model_validate(
            {
                "name": name,
                "email": email,
                "username": username,
                "hashed_password": hashed_password,
                "is_superuser": True,
                "profile_image_url": "https://www.imageurl.com/first_user.jpg",
                "tier_id": tier.id,
            }
        )

        # Creating first user/admin
        session.add(db_user)
        await session.commit()


async def main():
    async with local_session() as session:
        await create_first_user(session)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
