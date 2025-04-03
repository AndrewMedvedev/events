from fastapi import APIRouter, UploadFile

from src.classes import News
from src.responses import CustomResponse

router_news = APIRouter(prefix="/api/v1/news", tags=["news"])


@router_news.post("/add/")
async def add(
    title: str,
    body: str,
    image: UploadFile = None,
) -> CustomResponse:
    return await News().add_news(
        title=title,
        body=body,
        image=image,
    )


@router_news.get("/get/")
async def get(
    is_paginated: bool = False,
    page: int = 1,
    limit: int = 10,
) -> CustomResponse:
    return await News().get_news(
        is_paginated=is_paginated,
        page=page,
        limit=limit,
    )




@router_news.delete("/delete/{news_id}")
async def delete(
    news_id: int,
) -> CustomResponse:
    return await News().delete_news(news_id=news_id)
