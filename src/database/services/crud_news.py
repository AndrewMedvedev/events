import os

from sqlalchemy import select

from src.database.models import New
from src.database.schemas import NewsListResponse
from src.database.services.orm import DatabaseSessionService
from src.errors import DataBaseError
from src.interfaces import CRUDNewsBase


class CRUDNews(DatabaseSessionService, CRUDNewsBase):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def add_news(
        self,
        model: New,
    ) -> dict:
        async with self.session() as session:
            try:
                session.add(model)
                await session.commit()
                await session.refresh(model)
                return "done"
            except Exception:
                raise DataBaseError(
                    detail="create_news",
                )

    async def read_news(self) -> NewsListResponse:
        async with self.session() as session:
            news = await session.execute(select(New))
            try:
                return NewsListResponse(news=news.scalars().all())
            except Exception:
                raise DataBaseError(
                    detail="read_news",
                )

    async def read_news_with_limit(
        self,
        page: int = 1,
        limit: int = 5,
    ) -> NewsListResponse:
        offset = (page - 1) * limit
        async with self.session() as session:
            stmt = select(New).offset(offset).limit(limit)
            news = await session.execute(stmt)
        return NewsListResponse(news=news.scalars().all())

    async def delete_news(
        self,
        news_id: int,
    ) -> dict:
        async with self.session() as session:
            obj = await session.execute(select(New).filter(New.id == news_id))
            try:
                if obj:
                    data = obj.scalar()
                    if data.image != "absent":
                        os.remove(data.image)
                    await session.delete(data)
                    await session.commit()
                    return "done"
                raise DataBaseError(
                    detail="delete_news",
                )
            except Exception:
                raise DataBaseError(
                    detail="delete_news",
                )
