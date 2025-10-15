from contextlib import asynccontextmanager

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..dependencies import container
from .routers import router


@asynccontextmanager
async def lifespan(_: FastAPI): ...


def create_fastapi_app() -> FastAPI:
    app = FastAPI(title="Event service", lifespan=lifespan)
    setup_middleware(app)
    app.include_router(router)
    setup_dishka(container=container, app=app)
    return app


def setup_middleware(app: FastAPI) -> None:
    origins: list[str] = [
        "http://localhost:3000",
        "https://register-666-ramzer.onrender.com",
        "https://admin-panel-production-19ca.up.railway.app",
        "https://frontend-project-production-6352.up.railway.app",
        "https://admin-panel11.onrender.com",
        "https://online-service-for-applicants.onrender.com",
        "https://admin-panel2222.onrender.com",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
