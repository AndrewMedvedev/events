from io import BytesIO
from unittest.mock import AsyncMock, patch

from pytest import mark

from .conftest import generate_test_image
from .constant import (
    PATH_NEWS,
    TEST_BODY_NEWS,
    TEST_GET_ALL_NEWS,
    TEST_GET_NEWS_WITH_LIMIT,
    TEST_TITLE_NEWS,
)
from .requests import NewsAddTest, NewsGetParams, NewsListResponse, NewsResponse


@mark.parametrize(
    ("payload", "code"),
    [
        (
            NewsAddTest(
                title=TEST_TITLE_NEWS,
                body=TEST_BODY_NEWS,
                image=BytesIO(generate_test_image()).getvalue(),
            ),
            201,
        ),
        (
            NewsAddTest(
                title=TEST_TITLE_NEWS,
                body=TEST_BODY_NEWS,
            ),
            201,
        ),
    ],
)
def test_add_news_ok(client, payload, code):
    with patch("src.controllers.NewsControl.create_news", new_callable=AsyncMock):
        response = client.post(url=f"{PATH_NEWS}add", **payload.to_dict())

        assert response.status_code == code


@mark.parametrize(
    ("payload", "code"),
    [([], 422), ({}, 422), (None, 422)],
)
def test_add_news_bad(client, payload, code):
    with patch("src.controllers.NewsControl.create_news") as mock:
        mock_instance = mock.return_value
        mock_instance.create_news = AsyncMock()
        response = client.post(url=f"{PATH_NEWS}add", data=payload)

        assert response.status_code == code


@mark.parametrize(
    ("payload", "code"),
    [
        (NewsGetParams(is_paginated=False, page=1, limit=10), 200),
        (NewsGetParams(is_paginated=True, page=1, limit=10), 200),
    ],
)
def test_get_news_ok(client, payload, code):
    with patch("src.controllers.NewsControl.get_news", new_callable=AsyncMock) as mock:
        test_data = TEST_GET_ALL_NEWS
        if payload.is_paginated is True:
            test_data = TEST_GET_NEWS_WITH_LIMIT
        mock.return_value = NewsListResponse(
            news=[NewsResponse(**news) for news in test_data]
        )

        response = client.get(url=f"{PATH_NEWS}get", params=payload.to_dict())

        assert response.status_code == code


@mark.parametrize(
    ("payload", "code"),
    [({"is_paginated": ""}, 422), ({"page": ""}, 422), ({"limit": ""}, 422)],
)
def test_get_news_bad(client, payload, code):
    with patch("src.controllers.NewsControl.get_news", new_callable=AsyncMock) as mock:
        mock.return_value = NewsListResponse(
            news=[NewsResponse(**news) for news in TEST_GET_ALL_NEWS]
        )

        response = client.get(url=f"{PATH_NEWS}get", params=payload)

        assert response.status_code == code
