from fastapi import UploadFile

from ..database.crud import CRUD
from ..schemas import NewsListResponse, NewsSchema
from .image import Image


class NewsControl:
    def __init__(self) -> None:
        self.img = Image()

    async def create_news(self, schema: NewsSchema, image: UploadFile | None) -> None:
        img = None
        if image is not None:
            img = await self.img.add_image(image)

        schema.image = img
        return await CRUD().create_news(schema.to_model())

    async def get_news(self, is_paginated: bool, page: int, limit: int) -> NewsListResponse:
        if not is_paginated:
            return await CRUD().read_news()

        result = await CRUD().read_news_with_limit(page=page, limit=limit)
        for n in result.news:
            n.image = await self.img.get_image(path=n.image)
        return result

    @staticmethod
    async def delete_news(news_id: int) -> None:
        return await CRUD().delete_news(news_id=news_id)
