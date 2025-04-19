from pytest import mark

from src.schemas import NewsListResponse, NewsResponse

from .constant import (
    LEN_GET_ALL_NEWS,
    LEN_GET_WITH_LIMIT_NEWS,
    TEST_GET_ALL_NEWS,
    TEST_GET_NEWS_WITH_LIMIT,
)

pytestmark = [
    mark.asyncio,
]


async def test_get_all_news(news_mock):
    news_mock.get_news.return_value = NewsListResponse(
        news=[NewsResponse(**news) for news in TEST_GET_ALL_NEWS]
    )

    result = await news_mock.get_news(is_paginated=False, page=1, limit=5)

    assert len(result.news) == LEN_GET_ALL_NEWS


async def test_get_news_with_limit(news_mock):
    news_mock.get_news.return_value = NewsListResponse(
        news=[NewsResponse(**news) for news in TEST_GET_NEWS_WITH_LIMIT]
    )

    result = await news_mock.get_news(is_paginated=True, page=1, limit=3)

    assert len(result.news) == LEN_GET_WITH_LIMIT_NEWS
