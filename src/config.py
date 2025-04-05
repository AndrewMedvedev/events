from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:
    DB_HOST: str = config["DB_HOST"]
    DB_PORT: int = config["DB_PORT"]
    DB_NAME: str = config["DB_NAME"]
    DB_USER: str = config["DB_USER"]
    DB_PASSWORD: str = config["DB_PASSWORD"]

    GET_DATA: str = config["GET_DATA"]

    POSTGRES_HOST: str = config["POSTGRES_HOST"]
    POSTGRES_PORT: str = config["POSTGRES_PORT"]
    POSTGRES_PASSWORD: str = config["POSTGRES_PASSWORD"]
    POSTGRES_USER: str = config["POSTGRES_USER"]
    POSTGRES_DB: str = config["POSTGRES_DB"]


settings = Settings()


def get_db_url() -> str:
    return f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"


# def get_db_url() -> str:
#     return (
#         f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@"
#         f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
#     )
