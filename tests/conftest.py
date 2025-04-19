import io
from unittest.mock import MagicMock

from PIL import Image
from pytest import fixture

from .fixtures import client, event_mock, news_mock, visitor_mock

__all__ = [
    "client",
    "event_mock",
    "news_mock",
    "visitor_mock",
]


@fixture(autouse=True)
def mock_config(monkeypatch):
    mock_settings = MagicMock()
    mock_settings.POSTGRES_HOST = "localhost"
    mock_settings.POSTGRES_PORT = "5432"
    mock_settings.POSTGRES_PASSWORD = "12345"
    mock_settings.POSTGRES_USER = "user"
    mock_settings.POSTGRES_DB = "user_db"
    monkeypatch.setattr("config.Settings", mock_settings)


def generate_test_image():
    img = Image.new("RGB", (100, 100), color="red")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="JPEG")
    return img_byte_arr.getvalue()
