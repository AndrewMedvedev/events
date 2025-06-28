__all__ = [
    "add_events_fixture",
    "add_news_fixture",
    "client",
    "event_mock",
    "news_mock",
    "visitor_mock",
]


from .base import client, event_mock, news_mock, visitor_mock
from .structures import add_events_fixture, add_news_fixture
