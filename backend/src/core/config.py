# type: ignore

# Built-in Dependencies
from typing import Any, List
from enum import Enum
import os

# Third-Party Dependencies
from pydantic_core.core_schema import ValidationInfo
from pydantic import PostgresDsn, field_validator
from pydantic_settings import BaseSettings
from starlette.config import Config

# Environment Variables Config Getters
current_file_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.abspath(os.path.join(current_file_dir, "..", "..", ".env"))
config = Config(env_path)


class AppSettings(BaseSettings):
    PROJECT_NAME: str = config("PROJECT_NAME", default="Epsilon Stack")
    PROJECT_DESCRIPTION: str | None = config("PROJECT_DESCRIPTION", default=None)
    APP_VERSION: str | None = config("APP_VERSION", default="0.0.1")
    LICENSE_NAME: str | None = config("LICENSE_NAME", default=None)
    LICENSE_IDENTIFIER: str | None = config("LICENSE_IDENTIFIER", default=None)
    CONTACT_NAME: str | None = config("CONTACT_NAME", default=None)
    CONTACT_EMAIL: str | None = config("CONTACT_EMAIL", default=None)
    BASE_URL: str | None = config("BASE_URL", default=None)


class CryptSettings(BaseSettings):
    SECRET_KEY: str = config("SECRET_KEY")
    ALGORITHM: str = config("ALGORITHM", default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = config(
        "ACCESS_TOKEN_EXPIRE_MINUTES", default=1440
    )
    REFRESH_TOKEN_EXPIRE_DAYS: int = config("REFRESH_TOKEN_EXPIRE_DAYS", default=7)


class DatabaseSettings(BaseSettings):
    pass


class PostgresSettings(DatabaseSettings):
    POSTGRES_USER: str = config("POSTGRES_USER", default="postgres")
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD", default="postgres")
    POSTGRES_SERVER: str = config("POSTGRES_SERVER", default="localhost")
    POSTGRES_PORT: int = config("POSTGRES_PORT", default=5432)
    POSTGRES_DB: str = config("POSTGRES_DB", default="postgres")
    POSTGRES_ASYNC_URI: PostgresDsn | str = ""

    @field_validator("POSTGRES_ASYNC_URI", mode="after")
    def assemble_db_connection(cls, v: str | None, info: ValidationInfo) -> Any:
        if isinstance(v, str):
            if v == "":
                return PostgresDsn.build(
                    scheme="postgresql+asyncpg",
                    username=info.data["POSTGRES_USER"],
                    password=info.data["POSTGRES_PASSWORD"],
                    host=info.data["POSTGRES_SERVER"],
                    port=info.data["POSTGRES_PORT"],
                    path=info.data["POSTGRES_DB"],
                )
        return v


class FirstTierSettings(BaseSettings):
    TIER_NAME_DEFAULT: str = config("TIER_NAME_DEFAULT", default="Free")


class FirstUserSettings(BaseSettings):
    ADMIN_NAME: str = config("ADMIN_NAME", default="admin")
    ADMIN_EMAIL: str = config("ADMIN_EMAIL", default="admin@admin.com")
    ADMIN_USERNAME: str = config("ADMIN_USERNAME", default="admin")
    ADMIN_PASSWORD: str = config("ADMIN_PASSWORD", default="!Ch4ng3Th1sP4ssW0rd!")


class TestSettings(BaseSettings):
    TEST_NAME: str = config("TEST_NAME", default="Tester User")
    TEST_EMAIL: str = config("TEST_EMAIL", default="test@tester.com")
    TEST_USERNAME: str = config("TEST_USERNAME", default="testeruser")
    TEST_PASSWORD: str = config("TEST_PASSWORD", default="Str1ng$t")


class RedisCacheSettings(BaseSettings):
    REDIS_CACHE_HOST: str = config("REDIS_CACHE_HOST", default="localhost")
    REDIS_CACHE_PORT: int = config("REDIS_CACHE_PORT", default=6379)
    REDIS_CACHE_USERNAME: str = config("REDIS_CACHE_USERNAME", default="")
    REDIS_CACHE_PASSWORD: str = config("REDIS_CACHE_PASSWORD", default="nosecurity")
    REDIS_CACHE_URL: str = f"rediss://{REDIS_CACHE_USERNAME}:{REDIS_CACHE_PASSWORD}@{REDIS_CACHE_HOST}:{REDIS_CACHE_PORT}"

    @field_validator("REDIS_CACHE_URL", mode="after")
    def assemble_redis_cache_connection(
        cls, v: str | None, info: ValidationInfo
    ) -> Any:
        if isinstance(v, str):
            # If username and password are not set, use Redis URL connection string without security credentials
            if (
                info.data["REDIS_CACHE_USERNAME"] == ""
                and info.data["REDIS_CACHE_PASSWORD"] == ""
            ):
                return f"rediss://{info.data['REDIS_CACHE_HOST']}:{info.data['REDIS_CACHE_PORT']}"
            # If username and password are set, but without security, use Redis URL connection string without password
            if info.data["REDIS_CACHE_PASSWORD"] == "nosecurity":
                return f"rediss://{info.data['REDIS_CACHE_USERNAME']}@{info.data['REDIS_CACHE_HOST']}:{info.data['REDIS_CACHE_PORT']}"
        return v


class RedisQueueSettings(BaseSettings):
    REDIS_QUEUE_HOST: str = config("REDIS_QUEUE_HOST", default="")
    REDIS_QUEUE_PORT: int = config("REDIS_QUEUE_PORT", default=6379)
    REDIS_QUEUE_USERNAME: str = config("REDIS_QUEUE_USERNAME", default="")
    REDIS_QUEUE_PASSWORD: str = config("REDIS_QUEUE_PASSWORD", default="")
    REDIS_QUEUE_URL: str = f"rediss://{REDIS_QUEUE_USERNAME}:{REDIS_QUEUE_PASSWORD}@{REDIS_QUEUE_HOST}:{REDIS_QUEUE_PORT}"

    @field_validator("REDIS_QUEUE_URL", mode="after")
    def assemble_redis_queue_connection(
        cls, v: str | None, info: ValidationInfo
    ) -> Any:
        if isinstance(v, str):
            # If host is not set, use 'REDIS_CACHE_URL' as Redis Queue URL connection string
            if info.data["REDIS_QUEUE_HOST"] == "":
                redis_cache_settings = RedisCacheSettings()
                return redis_cache_settings.REDIS_CACHE_URL
            # If username and password are not set, use Redis URL connection string without security credentials
            if (
                info.data["REDIS_QUEUE_USERNAME"] == ""
                and info.data["REDIS_QUEUE_PASSWORD"] == ""
            ):
                return f"rediss://{info.data['REDIS_QUEUE_HOST']}:{info.data['REDIS_QUEUE_PORT']}"
            # If username and password are set, but without security, use Redis URL connection string without password
            if info.data["REDIS_QUEUE_PASSWORD"] == "nosecurity":
                return f"rediss://{info.data['REDIS_QUEUE_USERNAME']}@{info.data['REDIS_QUEUE_HOST']}:{info.data['REDIS_QUEUE_PORT']}"
        return v


class RedisRateLimiterSettings(BaseSettings):
    REDIS_RATE_LIMIT_HOST: str = config("REDIS_RATE_LIMIT_HOST", default="")
    REDIS_RATE_LIMIT_PORT: int = config("REDIS_RATE_LIMIT_PORT", default=6379)
    REDIS_RATE_LIMIT_USERNAME: str = config("REDIS_RATE_LIMIT_USERNAME", default="")
    REDIS_RATE_LIMIT_PASSWORD: str = config("REDIS_RATE_LIMIT_PASSWORD", default="")
    REDIS_RATE_LIMIT_URL: str = f"rediss://{REDIS_RATE_LIMIT_USERNAME}:{REDIS_RATE_LIMIT_PASSWORD}@{REDIS_RATE_LIMIT_HOST}:{REDIS_RATE_LIMIT_PORT}"

    @field_validator("REDIS_RATE_LIMIT_URL", mode="after")
    def assemble_redis_rate_limit_connection(
        cls, v: str | None, info: ValidationInfo
    ) -> Any:
        if isinstance(v, str):
            # If host is not set, use 'REDIS_CACHE_URL' as Redis Queue URL connection string
            if info.data["REDIS_RATE_LIMIT_HOST"] == "":
                redis_cache_settings = RedisCacheSettings()
                return redis_cache_settings.REDIS_CACHE_URL
            # If username and password are not set, use Redis URL connection string without security credentials
            if (
                info.data["REDIS_RATE_LIMIT_USERNAME"] == ""
                and info.data["REDIS_RATE_LIMIT_PASSWORD"] == ""
            ):
                return f"rediss://{info.data['REDIS_RATE_LIMIT_HOST']}:{info.data['REDIS_RATE_LIMIT_PORT']}"
            # If username and password are set, but without security, use Redis URL connection string without password
            if info.data["REDIS_RATE_LIMIT_PASSWORD"] == "nosecurity":
                return f"rediss://{info.data['REDIS_RATE_LIMIT_USERNAME']}@{info.data['REDIS_RATE_LIMIT_HOST']}:{info.data['REDIS_RATE_LIMIT_PORT']}"
        return v


class RedisHashSettings(BaseSettings):
    REDIS_HASH_SYSTEM_AUTH_VALID_USERNAMES: str = "system:auth:valid_usernames"


class DefaultRateLimitSettings(BaseSettings):
    DEFAULT_RATE_LIMIT_LIMIT: int = config("DEFAULT_RATE_LIMIT_LIMIT", default=10)
    DEFAULT_RATE_LIMIT_PERIOD: int = config("DEFAULT_RATE_LIMIT_PERIOD", default=3600)


class ClientSideCacheSettings(BaseSettings):
    CLIENT_CACHE_MAX_AGE: int = config("CLIENT_CACHE_MAX_AGE", default=60)


class CORSSettings(BaseSettings):
    CORS_ALLOW_ORIGINS: List[str] | str = config(
        "CORS_ALLOW_ORIGINS", default="*"
    ).split(",")
    CORS_ALLOW_METHODS: List[str] | str = config("CORS_ALLOW_METHODS", default="*").upper().split(",")  # fmt: skip
    CORS_ALLOW_HEADERS: List[str] | str = config(
        "CORS_ALLOW_HEADERS", default="*"
    ).split(",")
    CORS_ALLOW_CREDENTIALS: bool = config("CORS_ALLOW_CREDENTIALS", default="False").lower() == "true"  # fmt: skip
    CORS_EXPOSE_HEADERS: List[str] | str = config(
        "CORS_EXPOSE_HEADERS", default=""
    ).split(",")
    CORS_MAX_AGE: int = int(config("CORS_MAX_AGE", default="600"))


class MetricsSettings(BaseSettings):
    README_API_KEY: str = config("README_API_KEY", default="")
    README_BASE_LOG_URL: str = config("README_BASE_LOG_URL", default="")
    README_BUFFER_LENGTH: int = config("README_BUFFER_LENGTH", default=1)


class EnvironmentOption(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class EnvironmentSettings(BaseSettings):
    ENVIRONMENT: EnvironmentOption = config("ENVIRONMENT", default="development")


class Settings(
    AppSettings,
    PostgresSettings,
    CryptSettings,
    FirstUserSettings,
    FirstTierSettings,
    TestSettings,
    RedisCacheSettings,
    ClientSideCacheSettings,
    CORSSettings,
    MetricsSettings,
    RedisQueueSettings,
    RedisRateLimiterSettings,
    RedisHashSettings,
    DefaultRateLimitSettings,
    EnvironmentSettings,
):
    pass


settings = Settings()
