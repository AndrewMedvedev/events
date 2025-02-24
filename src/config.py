from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()


config = dotenv_values(env_path)


class Settings:
    DB_HOST: str = config["DB_HOST"]
    DB_PORT: int = config["DB_PORT"]
    DB_NAME: str = config["DB_NAME"]
    DB_USER: str = config["DB_USER"]
    DB_PASSWORD: str = config["DB_PASSWORD"]

    PASSWORD_GET_DATA: str = config["PASSWORD_GET_DATA"]

    GET_DATA: str = config["GET_DATA"]

    VALIDATE_ACCESS: str = config["VALIDATE_ACCESS"]
    VALIDATE_REFRESH: str = config["VALIDATE_REFRESH"]


settings = Settings()


def get_db_url() -> str:
    return (
        f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
        f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )
