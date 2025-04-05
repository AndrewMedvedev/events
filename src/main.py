import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database import config_logging
from src.errors import DataBaseError, ImageAddError, ImageGetError, SendError, db_error, image_add_error, image_get_error, send_error
from src.routers import router_event, router_news, router_visitors

config_logging(level=logging.INFO)

app = FastAPI(title="Админ панель личного аккаунта")

origins = [
    "http://localhost:3000",
    "https://register-666-ramzer.onrender.com",
    "https://admin-panel-production-19ca.up.railway.app",
    "https://frontend-project-production-6352.up.railway.app",
    "https://admin-panel11.onrender.com",
    "https://online-service-for-applicants.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.add_exception_handler(DataBaseError, db_error)

app.add_exception_handler(SendError, send_error)

app.add_exception_handler(ImageAddError, image_add_error)

app.add_exception_handler(ImageGetError, image_get_error)

app.include_router(router_event)

app.include_router(router_news)

app.include_router(router_visitors)
