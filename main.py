import uvicorn
from alembic import command
from alembic.config import Config

from src.api.app import create_fastapi_app, setup_errors_handlers, setup_middleware

app = create_fastapi_app()
setup_middleware(app)
setup_errors_handlers(app)

if __name__ == "__main__":
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    print("Миграции успешно применены.")
    uvicorn.run(app, host="0.0.0.0", port=8001)  # noqa: S104
