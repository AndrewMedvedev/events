from unittest.mock import AsyncMock

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture

from src.controllers import EventControl, NewsControl, VisitorsControl
from src.routers import events, news, visitors


@fixture
def client():
    app = FastAPI()

    app.include_router(events)
    app.include_router(news)
    app.include_router(visitors)

    return TestClient(app)


@fixture(name="event_mocks")
def event_mocks():
    controller = EventControl()
    controller.sql_event = AsyncMock()

    return controller


@fixture(name="news_mocks")
def news_mocks():
    controller = NewsControl()
    controller.sql_news = AsyncMock()
    controller.img = AsyncMock()

    return controller


@fixture(name="visitor_mocks")
def visitor_mocks():
    controller = VisitorsControl()
    controller.sql_visitor = AsyncMock()

    return controller
