from fastapi import APIRouter, status
from fastapi.datastructures import UploadFile
from fastapi.param_functions import File, Form
from fastapi.responses import JSONResponse, Response

from ..controllers import NewsControl
from ..schemas import NewsSchema

news = APIRouter(prefix="/api/v1/news", tags=["news"])


@news.post("/add/")
async def add(title: str = Form(), body: str = Form(), image: UploadFile | None = File()) -> Response:
    schema = NewsSchema(title=title, body=body)
    await NewsControl().create_news(schema, image)
    return Response(status_code=status.HTTP_201_CREATED)


@news.get("/get/")
async def get(is_paginated: bool = False, page: int = 1, limit: int = 10) -> Response:
    result = await NewsControl().get_news(
        is_paginated=is_paginated,
        page=page,
        limit=limit
    )
    return JSONResponse(status_code=status.HTTP_200_OK, content=result.to_dict())


@news.delete("/delete/{news_id}")
async def delete(news_id: int) -> Response:
    await NewsControl().delete_news(news_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
