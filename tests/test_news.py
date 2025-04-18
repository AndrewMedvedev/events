from pytest import mark

from src.schemas import NewsListResponse, NewsResponse

from .constant import (
    TEST_GET_ALL_NEWS,
    TEST_GET_NEWS_WITH_LIMIT,
)

pytestmark = [
    mark.asyncio,
]


async def test_get_all_news(news_mocks):
    news_mocks.sql_news.read_news.return_value = NewsListResponse(news=[NewsResponse(**news) for news in TEST_GET_ALL_NEWS])

    result = await news_mocks.get_news(is_paginated=False, page=1, limit=5)

    assert len(result.news) == 5


async def test_get_news_with_limit(news_mocks):
    news_mocks.sql_news.read_news_with_limit.return_value = NewsListResponse(news=[NewsResponse(**news) for news in TEST_GET_NEWS_WITH_LIMIT])

    result = await news_mocks.get_news(is_paginated=True, page=1, limit=3)

    assert len(result.news) == 3
