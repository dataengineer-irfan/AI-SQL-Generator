from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    ORACLE_USER: str
    ORACLE_PASSWORD: str
    ORACLE_DSN: str

    ORACLE_SYSDBA: bool = False

    GROQ_API_KEY: str

    DEFAULT_MODEL: str = "qwen/qwen3-32b"
    FALLBACK_MODEL_1: str = "qwen/qwen3-14b"
    FALLBACK_MODEL_2: str = "qwen/qwen3-8b"

    LOG_LEVEL: str = "INFO"

    TOP_K_SCHEMA: int = 5

    VECTOR_STORE_PATH: str = "vector_store"

    LOG_DIR: str = "logs"


settings = Settings()

Path(settings.LOG_DIR).mkdir(parents=True, exist_ok=True)
Path(settings.VECTOR_STORE_PATH).mkdir(parents=True, exist_ok=True)
