# Built-in Dependencies
from datetime import datetime, UTC

# Third-Party Dependencies
from redis.asyncio import Redis, ConnectionPool
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import FastAPI, APIRouter

# Local Dependencies
from src.core.logger import logging

# Logger instance for the current module
logger = logging.getLogger(__name__)

# Redis connection pool and client instances
pool: ConnectionPool | None = None
client: Redis | None = None


# Function to normalize a route path, removing query parameters
def normalize_route_path(route_path: str) -> str:
    """
    Normalize a route path by removing any query parameters.

    Args:
        route_path (str): The route path to be normalized.

    Returns:
        str: The normalized route path.

    Example:
        >>> normalize_route_path("/users?name=john")
        "/users"
    """
    return route_path.split("?")[0]


def sanitize_path(path: str) -> str:
    """
    Sanitizes a given path by normalizing it and replacing any forward slashes with underscores.

    Parameters:
        path (str): The path to be sanitized.

    Returns:
        str: The sanitized path.
    """
    normalized_path = normalize_route_path(path)
    return normalized_path.strip("/").replace("/", "_")


# Function to verify that a path is a valid route in the FastAPI application
def is_valid_path(path: str, app: FastAPI) -> bool:
    """
    Checks if a given path is a valid route in the FastAPI application.

    Parameters:
        path (str): The path to be checked.
        app (FastAPI): The FastAPI application instance.

    Returns:
        bool: True if the path is a valid route, False otherwise.
    """
    # Obtains all application routes
    all_routes = [sanitize_path(route.path) for route in app.routes]
    return path in all_routes


# Checks if a rate limit has been exceeded
async def is_rate_limited(
    app: FastAPI,
    db: AsyncSession,
    user_id: int,
    path: str,
    limit: int,
    period: int,
) -> bool:
    """
    Check if the user with the given ID is rate limited for the specified path.

    Args:
        app (FastAPI): The FastAPI application instance.
        db (AsyncSession): The asynchronous session for interacting with the database.
        user_id (int): The ID of the user to check for rate limiting.
        path (str): The path to check for rate limiting.
        limit (int): The maximum number of requests allowed within the specified period.
        period (int): The duration of the rate limiting period in seconds.

    Returns:
        bool: True if the user is rate limited, False otherwise.
    """
    if client is None:
        logger.error("Redis client is not initialized.")
        raise Exception("Redis client is not initialized.")

    # Calculate the start of the current time window
    current_timestamp = int(datetime.now(UTC).timestamp())
    window_start = current_timestamp - (current_timestamp % period)

    # Checks if the path is a valid route
    if not is_valid_path(path=path, app=app):
        logger.warning(f"Invalid route: {path}")
        return False

    # Sanitize the path for use in the key
    sanitized_path = sanitize_path(path)
    key = f"ratelimit:{user_id}:{sanitized_path}:{window_start}"

    try:
        # Increment the count for the current time window and set the expiration if it's a new window
        current_count = await client.incr(key)
        if current_count == 1:
            await client.expire(key, period)

        # Check if the current count exceeds the rate limit
        if current_count > limit:
            return True

    except Exception as e:
        logger.exception(f"Error checking rate limit for user {user_id} on path {path}: {e}")
        raise e

    return False
