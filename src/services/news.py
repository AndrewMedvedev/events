from fastapi import UploadFile

from ..core.domain import NewsSchema
from ..database.repository import NewsRepository
from ..utils import Images


class NewsService:
    def __init__(self, repository: NewsRepository) -> None:
        self.repository = repository
        self.img = Images()

    async def create_news(self, schema: NewsSchema, image: UploadFile | None) -> NewsSchema:
        img = None
        if image is not None:
            img = await self.img.add_images(image)

        schema.image = img
        return await self.repository.create(schema)

    async def get_news(self, page: int, limit: int) -> list[NewsSchema]:
        result = await self.repository.read_all(limit, page)
        for n in result:
            if n.image is not None:
                n.image = await self.img.get_images(path=n.image)
        return result

    async def delete_news(self, news_id: int) -> None:
        return await self.repository.delete_news(news_id)
