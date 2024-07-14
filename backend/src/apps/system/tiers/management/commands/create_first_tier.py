# Built-in Dependencies
import asyncio

# Third-Party Dependencies
from sqlmodel import select

# Local Dependencies
from src.core.db.session import AsyncSession, local_session
from src.apps.system.tiers.models import Tier
from src.core.config import settings


async def create_first_tier(session: AsyncSession) -> None:
    # First tier data
    default_tier_name = settings.TIER_NAME_DEFAULT

    # Checking if tier already exists
    query = select(Tier).where(Tier.default == True)
    result = await session.exec(query)
    tier = result.one_or_none()

    if tier is not None and tier.name != default_tier_name:
        raise Exception(
            f"The current value of the TIER_NAME_DEFAULT environment variable is '{settings.TIER_NAME_DEFAULT}', but a default tier already exists in the database with the name '{tier.name}'. Please adjust this before proceeding."
        )

    # Creating tier if it doesn't exist
    if tier is None:
        # Validating tier data
        # See: https://github.com/tiangolo/sqlmodel/issues/52#issuecomment-1311987732
        tier_db = Tier.model_validate({"name": default_tier_name, "default": True})

        # Creating default tier
        session.add(tier_db)
        await session.commit()


async def main():
    async with local_session() as session:
        await create_first_tier(session)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
