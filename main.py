from contextlib import asynccontextmanager

import uvicorn
from alembic import command
from alembic.config import Config
from fastapi import FastAPI

from src.api.app import create_fastapi_app, setup_errors_handlers, setup_middleware


@asynccontextmanager
async def lifespan(_: FastAPI):
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    print("Миграции успешно применены.")
    yield


app = create_fastapi_app(lifespan)
setup_middleware(app)
setup_errors_handlers(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)  # noqa: S104
