from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str

    database_url: str

    database_url_test: str

    supabase_url: str

    supabase_publishable_key: str

    supabase_bucket: str

    environment: str

    timezone: str

    openweather_api_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="ATL_",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()