"""Module with config from .env for app."""

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    """Base config of app."""

    model_config = SettingsConfigDict(
        env_file='../.env',
        env_file_encoding='utf-8',
    )

    repo_url: str = Field(alias='REPO_URL')
