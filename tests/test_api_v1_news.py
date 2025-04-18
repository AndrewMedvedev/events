from io import BytesIO
from unittest.mock import AsyncMock, patch

from pytest import mark

from src.schemas import NewsListResponse, NewsResponse

from .conftest import generate_test_image
from .constant import (
    PATH_NEWS,
    TEST_BODY_NEWS,
    TEST_GET_ALL_NEWS,
    TEST_GET_NEWS_WITH_LIMIT,
    TEST_TITLE_NEWS,
)

pytestmark = [
    mark.asyncio,
]


@mark.parametrize(
    ("payload", "image", "code"),
    [
        (
            {
                "title": TEST_TITLE_NEWS,
                "body": TEST_BODY_NEWS,
            },
            BytesIO(generate_test_image()),
            201,
        ),
        (
            {
                "title": TEST_TITLE_NEWS,
                "body": TEST_BODY_NEWS,
            },
            None,
            201,
        ),
    ],
)
async def test_add_news(client, payload, image, code):
    with patch("src.controllers.NewsControl.create_news") as mock:
        mock_instance = mock.return_value
        mock_instance.create_news = AsyncMock()
        request_data = {"data": payload}
        if image:
            request_data["files"] = {"image": ("test.jpg", image, "image/jpeg")}
        response = client.post(url=f"{PATH_NEWS}add", **request_data)

        assert response.status_code == code


@mark.parametrize(
    ("payload", "code"),
    [
        (
            {
                "is_paginated": "false",
                "page": 1,
                "limit": 5,
            },
            200,
        ),
    ],
)
async def test_get_all_news(client, payload, code):
    with patch("src.controllers.NewsControl.get_news", new_callable=AsyncMock) as mock:
        mock.return_value = NewsListResponse(news=[NewsResponse(**news) for news in TEST_GET_ALL_NEWS])

        response = client.get(url=f"{PATH_NEWS}get", params=payload)

        assert response.status_code == code


@mark.parametrize(
    ("payload", "code"),
    [
        (
            {
                "is_paginated": "true",
                "page": 1,
                "limit": 3,
            },
            200,
        ),
    ],
)
async def test_get_news_with_limit(client, payload, code):
    with patch("src.controllers.NewsControl.get_news", new_callable=AsyncMock) as mock:
        mock.return_value = NewsListResponse(news=[NewsResponse(**news) for news in TEST_GET_NEWS_WITH_LIMIT])

        response = client.get(url=f"{PATH_NEWS}get", params=payload)

        assert response.status_code == code
