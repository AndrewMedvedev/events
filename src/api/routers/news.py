from dishka.integrations.fastapi import DishkaRoute
from dishka.integrations.fastapi import FromDishka as Depends
from fastapi import APIRouter, status
from fastapi.datastructures import UploadFile
from fastapi.param_functions import File, Form

from ...core.domain import NewsSchema
from ...services.news import NewsService

news = APIRouter(route_class=DishkaRoute, prefix="/news", tags=["news"])


@news.post("/add/", status_code=status.HTTP_201_CREATED)
async def add(
    service: Depends[NewsService],
    title: str = Form(),
    body: str = Form(),
    image: UploadFile | None = File(default=None),
) -> None:
    schema = NewsSchema(title=title, body=body)
    await service.create_news(schema, image)


@news.get("/get/", status_code=status.HTTP_200_OK)
async def get(service: Depends[NewsService], page: int = 1, limit: int = 10) -> list[NewsSchema]:
    return await service.get_news(page=page, limit=limit)


@news.delete("/delete/{news_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(service: Depends[NewsService], news_id: int) -> None:
    await service.delete_news(news_id)
