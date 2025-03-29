from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.classes import News
from src.database.schemas import NewsModel

router_news = APIRouter(prefix="/api/v1/news", tags=["news"])


@router_news.post("/add/")
async def add(model: NewsModel) -> JSONResponse:
    return await News().create_news(model=model)


@router_news.get("/get/")
async def get() -> JSONResponse:
    return await News().get_news()


@router_news.delete("/delete/{news_id}")
async def delete(
    news_id: int,
) -> JSONResponse:
    return await News().delete_news(news_id=news_id)
