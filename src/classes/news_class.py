from fastapi.responses import JSONResponse
from src.interfaces import NewsBase
from src.database.services.crud import CRUD
from src.database.schemas import NewsModel
from src.database.models import New


class News(NewsBase):

    def __init__(self) -> None:
        self.crud = CRUD()

    async def create_news(
        self,
        model: NewsModel,
    ) -> JSONResponse:
        data = New(
            body=model.body,
            image=model.image,
        )
        return JSONResponse(content=await self.crud.create_news(data))

    async def get_news(self) -> list[dict]:
        return await self.crud.get_news()

    async def delete_news(
        self,
        news_id: int,
    ) -> JSONResponse:
        return JSONResponse(content=await self.crud.delete_news(news_id=news_id))
