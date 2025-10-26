import logging

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from ..core.exceptions import (
    AlreadyExistsError,
    CreationError,
    DeletionError,
    NoPlacesError,
    ReadingError,
)
from ..dependencies import container
from .routers import router

logger = logging.getLogger(__name__)


def create_fastapi_app() -> FastAPI:
    app = FastAPI(title="Event service")
    setup_middleware(app)
    app.include_router(router)
    setup_dishka(container=container, app=app)
    return app


def setup_middleware(app: FastAPI) -> None:
    origins: list[str] = [
        "https://admin-panel-1-y4b1.onrender.com",
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


def setup_errors_handlers(app: FastAPI) -> None:
    @app.exception_handler(CreationError)
    def handle_creation_error(
        request: Request,  # noqa: ARG001
        exc: CreationError,
    ) -> JSONResponse:
        logger.error(exc)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Error while resource creation"},
        )

    @app.exception_handler(ReadingError)
    def handle_reading_error(
        request: Request,  # noqa: ARG001
        exc: ReadingError,
    ) -> JSONResponse:
        logger.error(exc)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Error while resource reading"},
        )

    @app.exception_handler(AlreadyExistsError)
    def handle_already_exists_error(
        request: Request,  # noqa: ARG001
        exc: AlreadyExistsError,
    ) -> JSONResponse:
        logger.error(exc)
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT, content={"detail": "Resource already exists"}
        )

    @app.exception_handler(DeletionError)
    def handle_deletion_error(
        request: Request,  # noqa: ARG001
        exc: DeletionError,
    ) -> JSONResponse:
        logger.error(exc)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Error while resource deletion"},
        )

    @app.exception_handler(NoPlacesError)
    def handle_no_places_error(
        request: Request,  # noqa: ARG001
        exc: NoPlacesError,
    ) -> JSONResponse:
        logger.error(exc)
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": "Error no places"},
        )
