from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import router_event, router_visitors

app = FastAPI(title="Админ панель личного аккаунта")

app.include_router(router_event)

app.include_router(router_visitors)

origins = [
    "http://localhost:3000",
    "https://register-666-ramzer.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
