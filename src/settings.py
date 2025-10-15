from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# Корневая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent
# Секретные переменные
ENV_PATH = BASE_DIR / ".env"


load_dotenv(ENV_PATH)


class PostgresSettings(BaseSettings):
    host: str = ""
    port: int = 5342
    password: str = ""
    user: str = ""
    db: str = ""

    model_config = SettingsConfigDict(env_prefix="POSTGRES_")

    @property
    def url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"
        )


class GetDataSettings(BaseSettings):
    get_data: str = ""


class Settings(BaseSettings):
    postgres: PostgresSettings = PostgresSettings()
    get_data: GetDataSettings = GetDataSettings()


settings = Settings()
