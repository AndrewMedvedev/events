import logging

from fastapi import UploadFile, status

from src.database.models import New
from src.database.services import CRUDNews
from src.interfaces import NewsBase
from src.responses import CustomResponse

from .images_class import Images

log = logging.getLogger(__name__)


class News(NewsBase):
    IMAGE_FOLDER = "images"

    def __init__(self) -> None:
        self.crud = CRUDNews()
        self.img = Images()

    async def add_news(
        self,
        title: str,
        body: str,
        image: UploadFile,
    ) -> CustomResponse:
        log.info("Вызвана функция add_news")
        data = New(
            title=title,
            body=body,
            image=await self.img.add_image(image=image),
        )
        return CustomResponse(
            status_code=status.HTTP_201_CREATED,
            body=await self.crud.add_news(data),
        )

    async def get_news(
        self,
        is_paginated: bool,
        page: int,
        limit: int,
    ) -> CustomResponse:
        log.info("Вызвана функция get_news")
        if is_paginated:
            all_news = await self.crud.read_news_with_limit(
                page=page,
                limit=limit,
            )
            lst_news = {"news": []}
            for i in (all_news.model_dump()).get("news"):
                img_base64 = await self.img.get_image(path=i.get("image"))
                del i["image"]
                i["image"] = img_base64
                lst_news["news"].append(i)
            return CustomResponse(
                status_code=status.HTTP_200_OK,
                body=lst_news,
            )
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=await self.crud.read_news(),
        )

    async def delete_news(
        self,
        news_id: int,
    ) -> CustomResponse:
        log.info("Вызвана функция delete_news")
        return CustomResponse(
            status_code=status.HTTP_204_NO_CONTENT,
            body=await self.crud.delete_news(news_id=news_id),
        )
