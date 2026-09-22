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
    CORS_ORIGINS: List[str] = ['http://localhost:5173', 'http://localhost:3000']

    model_config = SettingsConfigDict(
        env_file=os.path.join(PARENT_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
