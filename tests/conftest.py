import io

from PIL import Image

from .fixtures import (
    client,
    event_mocks,
    news_mocks,
    visitor_mocks,
)

__all__ = [
    "client",
    "event_mocks",
    "news_mocks",
    "visitor_mocks",
]


def generate_test_image():
    img = Image.new("RGB", (100, 100), color="red")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="JPEG")
    return img_byte_arr.getvalue()
