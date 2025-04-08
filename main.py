from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import events, news, visitors

app = FastAPI(title="Admin Panel")

origins: list[str] = [
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


def include_routers(app: FastAPI):
    app.include_router(events)
    app.include_router(news)
    app.include_router(visitors)


include_routers(app)
