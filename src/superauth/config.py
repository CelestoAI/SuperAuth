from typing import Optional

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """Centralized configuration class for all environment variables using Pydantic Settings."""

    apollo_api_key: Optional[SecretStr] = Field("", env="APOLLO_API_KEY")
    celesto_api_key: Optional[SecretStr] = Field("", env="CELESTO_API_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        extra = "ignore"


# Create a global config instance
config = Config()
