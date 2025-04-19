from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:
    GET_DATA: str = config.get("GET_DATA", "")

    POSTGRES_HOST: str = config.get("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = config.get("POSTGRES_PORT", "5432")
    POSTGRES_PASSWORD: str = config.get("POSTGRES_PASSWORD", "12345")
    POSTGRES_USER: str = config.get("POSTGRES_USER", "user")
    POSTGRES_DB: str = config.get("POSTGRES_DB", "user_db")


def get_db_url() -> str:
    return f"postgresql+asyncpg://{Settings.POSTGRES_USER}:{Settings.POSTGRES_PASSWORD}@{Settings.POSTGRES_HOST}:{Settings.POSTGRES_PORT}/{Settings.POSTGRES_DB}"
