from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient
from pytest import fixture

from main import app
from src.schemas import EventListResponse, NewsListResponse, UserEventSchema


@fixture
def client():
    return TestClient(app)


@fixture
def event_mock():
    with patch("src.controllers.EventControl") as mock:
        instance = mock.return_value
        instance.sql_event = AsyncMock()
        instance.get_event = AsyncMock(return_value=EventListResponse(events=[]))
        yield instance


@fixture
def news_mock():
    with patch("src.controllers.NewsControl") as mock:
        instance = mock.return_value
        instance.sql_news = AsyncMock()
        instance.get_news = AsyncMock(return_value=NewsListResponse(news=[]))
        yield instance


@fixture
def visitor_mock():
    with patch("src.controllers.VisitorControl") as mock:
        instance = mock.return_value
        instance.sql_visitor = AsyncMock()
        instance.get_user_events = AsyncMock(return_value=UserEventSchema(user_event=[]))
        yield instance
