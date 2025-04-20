from io import BytesIO

from pytest import mark, raises

from src.exeptions import BadRequestHTTPError
from src.schemas import NewsListResponse, NewsResponse
from tests.conftest import generate_test_image
from tests.requests import NewsAddTest, NewsGetParams

from .constant import (
    LEN_GET_ALL_NEWS,
    LEN_GET_WITH_LIMIT_NEWS,
    TEST_BODY_NEWS,
    TEST_GET_ALL_NEWS,
    TEST_GET_NEWS_WITH_LIMIT,
    TEST_TITLE_NEWS,
)


@mark.parametrize(
    ("payload"),
    [
        (
            NewsAddTest(
                title=TEST_TITLE_NEWS,
                body=TEST_BODY_NEWS,
                image=BytesIO(generate_test_image()).getvalue(),
            ),
        ),
        (
            NewsAddTest(
                title=TEST_TITLE_NEWS,
                body=TEST_BODY_NEWS,
            ),
        ),
    ],
)
def test_control_create_news_ok(news_mock, payload):
    news_mock.create_news.return_value = None
    result = news_mock.create_news(payload)
    assert result is None


@mark.asyncio
@mark.parametrize(
    ("payload"),
    [([],), ({},), (None,)],
)
async def test_control_create_news_bad(news_mock, payload):
    news_mock.create_news.side_effect = BadRequestHTTPError
    with raises(BadRequestHTTPError):
        await news_mock.create_news(payload)


@mark.asyncio
@mark.parametrize(
    ("payload"),
    [
        (NewsGetParams(is_paginated=False, page=1, limit=10)),
        (NewsGetParams(is_paginated=True, page=1, limit=10)),
    ],
)
async def test_control_get_news_ok(news_mock, payload):
    test_data = TEST_GET_ALL_NEWS
    result_data = LEN_GET_ALL_NEWS
    if payload.is_paginated is not False:
        test_data = TEST_GET_NEWS_WITH_LIMIT
        result_data = LEN_GET_WITH_LIMIT_NEWS
    news_mock.get_news.return_value = NewsListResponse(
        news=[NewsResponse(**news) for news in test_data]
    )

    result = await news_mock.get_news(payload)

    assert len(result.news) == result_data


@mark.asyncio
@mark.parametrize(
    ("payload"),
    [({"is_paginated": ""}), ({"page": ""}), ({"limit": ""})],
)
async def test_control_get_news_bad(news_mock, payload):
    news_mock.get_news.side_effect = BadRequestHTTPError
    with raises(BadRequestHTTPError):
        await news_mock.get_news(payload)


@mark.parametrize(("news_id"), [(1,), (11,)])
def test_control_delete_news_ok(news_mock, news_id):
    news_mock.delete_news.return_value = None
    result = news_mock.delete_news(news_id)
    assert result is None


@mark.parametrize(("news_id"), [([],), ({},), (None,)])
def test_control_delete_news_bad(news_mock, news_id):
    news_mock.delete_news.side_effect = BadRequestHTTPError
    with raises(BadRequestHTTPError):
        news_mock.delete_news(news_id)
