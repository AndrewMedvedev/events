from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.errors import DataBaseError, SendError
from src.routers import router_event, router_visitors

app = FastAPI(title="Админ панель личного аккаунта")

app.include_router(router_event)

app.include_router(router_visitors)

origins = [
    "http://localhost:3000",
    "https://register-666-ramzer.onrender.com",
    "https://admin-panel-production-19ca.up.railway.app",
    "https://frontend-project-production-6352.up.railway.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.exception_handler(DataBaseError)
async def db_error(
    request: Request,
    exc: DataBaseError,
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": str(exc)},
    )


@app.exception_handler(SendError)
async def send_error(
    request: Request,
    exc: SendError,
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": str(exc)},
    )
