from pathlib import Path
from typing import Optional

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # Oracle (optional for now)
    ORACLE_USER: Optional[str] = None
    ORACLE_PASSWORD: Optional[str] = None
    ORACLE_DSN: Optional[str] = None

    ORACLE_SYSDBA: bool = False

    # LLM
    GROQ_API_KEY: str

    DEFAULT_MODEL: str = "qwen/qwen3-32b"
    FALLBACK_MODEL_1: str = "qwen/qwen3-14b"
    FALLBACK_MODEL_2: str = "qwen/qwen3-8b"

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_DIR: str = "logs"

    # RAG
    TOP_K_SCHEMA: int = 5
    VECTOR_STORE_PATH: str = "vector_store"


settings = Settings()

Path(settings.LOG_DIR).mkdir(
    parents=True,
    exist_ok=True
)

Path(settings.VECTOR_STORE_PATH).mkdir(
    parents=True,
    exist_ok=True
)