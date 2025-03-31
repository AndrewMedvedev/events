from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse

from src.classes import News
from src.responses import CustomResponse

router_news = APIRouter(prefix="/api/v1/news", tags=["news"])


@router_news.post("/add/")
async def add(
    head: str,
    body: str,
    image: UploadFile = None,
) -> CustomResponse:
    return await News().add_news(
        head=head,
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


@router_news.get("/get/image/{image_name}")
async def get_image(image_name: str) -> FileResponse:
    return await News().get_image(
        image_name=image_name,
    )


@router_news.delete("/delete/{news_id}")
async def delete(
    news_id: int,
) -> CustomResponse:
    return await News().delete_news(news_id=news_id)
