import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    CH_URL: str = os.getenv("CH_URL", "")
    MYSQL_URL: str = os.getenv("MYSQL_URL", "")
    MYSQL_URL_SYNC: str = os.getenv("MYSQL_URL_SYNC", "")
    PLATFORM: str = os.getenv("PLATFORM", "")
    TZ: str = os.getenv("TZ", "")  # noqa: CCE001
    POSTGRES_ASYNC_URL: str = os.getenv("POSTGRES_ASYNC_URL", "")  # noqa: CCE001
    POSTGRES_SYNC_URL: str = os.getenv("POSTGRES_SYNC_URL", "")  # noqa: CCE001
    PG_SCHEMA: str = os.getenv("PG_SCHEMA", "")  # noqa: CCE001
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "")  # noqa: CCE001
    SENTRY_DSN: str = os.getenv("SENTRY_DSN", "")  # noqa: CCE001
    SENTRY_ENV: str = os.getenv("SENTRY_ENV", "")  # noqa: CCE001
    TEST_STAND: bool = bool(os.getenv("TEST_STAND", default=False))  # noqa: CCE001
    METABASE_CLIENT_TIMEOUT: int = int(
        os.getenv("METABASE_CLIENT_TIMEOUT", default=20)
    )  # noqa: CCE001
    METABASE_URL: str = os.getenv("METABASE_URL", "")  # noqa: CCE001
    METABASE_USERNAME: str = os.getenv("METABASE_USERNAME", "")  # noqa: CCE001
    METABASE_PASS: str = os.getenv("METABASE_PASS", "")  # noqa: CCE001


@lru_cache
def get_settings() -> Settings:
    return Settings()
