from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    SERVICE_NAME: str = "bigbrowser-api"
    SERVICE_VERSION: str = "0.1.0"
    API_PREFIX: str = "/api/v1"

    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
