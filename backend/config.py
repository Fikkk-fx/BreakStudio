import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BACKEND_DIR)

class Settings(BaseSettings):
    PRUNA_AI_API_KEY: str = ""
    UPLOAD_DIR: str = os.path.join(BACKEND_DIR, 'uploads')
    OUTPUT_DIR: str = os.path.join(BACKEND_DIR, 'outputs')
    DATABASE_PATH: str = os.path.join(BACKEND_DIR, 'director.db')

    # Comma-separated list of allowed CORS origins.
    # Set CORS_ORIGINS env var to add production URLs e.g.:
    #   CORS_ORIGINS=https://your-app.vercel.app,http://localhost:5173
    CORS_ORIGINS: str = "http://localhost:5173,http://localhost:3000"

    model_config = SettingsConfigDict(
        env_file=os.path.join(PARENT_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def cors_origins_list(self) -> List[str]:
        """Parse CORS_ORIGINS string into a list, stripping whitespace."""
        return [origin.strip() for origin in self.CORS_ORIGINS.split(',') if origin.strip()]

settings = Settings()
