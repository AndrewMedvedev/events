import os

from fastapi import UploadFile, status
from fastapi.responses import FileResponse

from src.database.controls import add_image
from src.database.models import New
from src.database.services import CRUDNews
from src.interfaces import NewsBase
from src.responses import CustomResponse


class News(NewsBase):

    IMAGE_FOLDER = "images"

    def __init__(self) -> None:
        self.crud = CRUDNews()

    async def add_news(
        self,
        head: str,
        body: str,
        image: UploadFile,
    ) -> CustomResponse:
        data = New(
            head=head,
            body=body,
            image=await add_image(image=image),
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
        if is_paginated:
            return CustomResponse(
                status_code=status.HTTP_200_OK,
                body=await self.crud.read_news_with_limit(
                    page=page,
                    limit=limit,
                ),
            )
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=await self.crud.read_news(),
        )

    async def get_image(
        self,
        image_name: str,
    ) -> FileResponse:
        return FileResponse(os.path.join(image_name))

    async def delete_news(
        self,
        news_id: int,
    ) -> CustomResponse:
        return CustomResponse(
            status_code=status.HTTP_204_NO_CONTENT,
            body=await self.crud.delete_news(news_id=news_id),
        )
