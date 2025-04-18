from fastapi import UploadFile

from ..database.crud import SQLNews
from ..schemas import NewsListResponse, NewsSchema
from ..utils import Images


class NewsControl:
    def __init__(self) -> None:
        self.sql_news = SQLNews()
        self.img = Images()

    async def create_news(self, schema: NewsSchema, image: UploadFile | None) -> None:
        img = None
        if image is not None:
            img = await self.img.add_images(image)

        schema.image = img
        return await self.sql_news.create_news(schema.to_model())

    async def get_news(self, is_paginated: bool, page: int, limit: int) -> NewsListResponse:
        if not is_paginated:
            return await self.sql_news.read_news()

        result = await self.sql_news.read_news_with_limit(page=page, limit=limit)
        for n in result.news:
            if n.image is not None:
                n.image = await self.img.get_images(path=n.image)
        return result

    async def delete_news(self, news_id: int) -> None:
        return await self.sql_news.delete_news(news_id=news_id)
