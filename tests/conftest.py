import io

from PIL import Image

from .fixtures import client, event_mock, init_config, news_mock, visitor_mock

__all__ = [
    "client",
    "event_mock",
    "init_config",
    "news_mock",
    "visitor_mock",
]


def generate_test_image():
    img = Image.new("RGB", (100, 100), color="red")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="JPEG")
    return img_byte_arr.getvalue()
