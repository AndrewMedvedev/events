from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()


def load_config() -> dict:
    env_path = find_dotenv(".env")

    if not env_path:
        env_path = find_dotenv(".test.env")

    return dotenv_values(env_path)


config = load_config()


class Settings:
    GET_DATA: str = config["GET_DATA"]

    POSTGRES_HOST: str = config["POSTGRES_HOST"]
    POSTGRES_PORT: str = config["POSTGRES_PORT"]
    POSTGRES_PASSWORD: str = config["POSTGRES_PASSWORD"]
    POSTGRES_USER: str = config["POSTGRES_USER"]
    POSTGRES_DB: str = config["POSTGRES_DB"]


def get_db_url() -> str:
    return f"postgresql+asyncpg://{Settings.POSTGRES_USER}:{Settings.POSTGRES_PASSWORD}@{Settings.POSTGRES_HOST}:{Settings.POSTGRES_PORT}/{Settings.POSTGRES_DB}"
