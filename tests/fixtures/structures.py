import io
from datetime import UTC, datetime

from PIL import Image
from pytest import fixture

from .requests import EventSchema, NewsAddTest


def generate_test_image():
    img = Image.new("RGB", (100, 100), color="red")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="JPEG")
    return img_byte_arr.getvalue()


@fixture
def add_events_fixture() -> EventSchema:
    return EventSchema(
        name_event="names",
        date_time=(datetime.now(tz=UTC)),
        location="streets",
        description="descriptions",
        points_for_the_event=11,
        limit_people=411,
    )


@fixture
def add_news_fixture() -> NewsAddTest:
    return NewsAddTest(
        title="Test News Title",
        body="This is a test news body",
        image=io.BytesIO(generate_test_image()).getvalue(),
    )
