from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:

    GET_DATA: str = config["GET_DATA"]

    POSTGRES_HOST: str = config["POSTGRES_HOST"]
    POSTGRES_PORT: str = config["POSTGRES_PORT"]
    POSTGRES_PASSWORD: str = config["POSTGRES_PASSWORD"]
    POSTGRES_USER: str = config["POSTGRES_USER"]
    POSTGRES_DB: str = config["POSTGRES_DB"]


def get_db_url() -> str:
    return f"postgresql+asyncpg://{Settings.POSTGRES_USER}:{Settings.POSTGRES_PASSWORD}@{Settings.POSTGRES_HOST}:{Settings.POSTGRES_PORT}/{Settings.POSTGRES_DB}"
