import base64
import io
import os
import uuid

from fastapi import UploadFile
from PIL import Image

from .constants import FOLDER
from .db.crud import (create_event, create_news, create_visitor, delete_event,
                      delete_news, delete_visitor, get_visitors_events,
                      read_event, read_events_with_limit, read_news,
                      read_news_with_limit, verify_visitor)
from .exceptions import UserDataNotFoundError
from .rest import get_user_data
from .schemas import (EventListResponse, EventSchema, NewsListResponse,
                      NewsSchema, UserEventSchema, VisitorSchema)


class EventControl:

    @staticmethod
    async def create_event(schema: EventSchema) -> None:
        return await create_event(schema.to_model())

    @staticmethod
    async def get_event(is_paginated: bool, page: int, limit: int) -> EventListResponse:
        if not is_paginated:
            return await read_event()
        return await read_events_with_limit(page=page, limit=limit)

    @staticmethod
    async def delete_event(model_id: int) -> None:
        return await delete_event(model_id=model_id)


class ImageControl:

    @staticmethod
    async def add_image(image: UploadFile) -> str:
        dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), FOLDER)
        os.makedirs(dir, exist_ok=True)
        file_name = os.path.join(FOLDER, f"{uuid.uuid4()}{os.path.splitext(image.filename)[1]}")
        contents = await image.read()
        img = Image.open(io.BytesIO(contents))
        img.save(file_name, format="JPEG", optimize=True, quality=90)
        return file_name

    @staticmethod
    async def get_image(path: str):
        if path != "absent":
            with open(path, "rb") as file:
                img_bytes = file.read()
                return base64.b64encode(img_bytes).decode("ascii")
        else:
            return "absent"


class NewsControl:

    def __init__(self) -> None:
        self.img = ImageControl()

    async def create_news(self, schema: NewsSchema, image: UploadFile | None) -> None:
        img = None
        if image is not None:
            img = await self.img.add_image(image)

        schema.image = img
        return await create_news(schema.to_model())

    async def get_news(self, is_paginated: bool, page: int, limit: int) -> NewsListResponse:
        if not is_paginated:
            return await read_news()

        result = await read_news_with_limit(page=page, limit=limit)
        for n in result.news:
            n.image = await self.img.get_image(path=n.image)
        return result

    @staticmethod
    async def delete_news(news_id: int) -> None:
        return await delete_news(news_id=news_id)


class VisitorsControl:

    @staticmethod
    async def create_user(user_id: int, event_id: int) -> None:
        if (data := await get_user_data(user_id)).get("body") is None:
            raise UserDataNotFoundError("User data not found or invalid")

        result = VisitorSchema.create({
            "user_id": user_id,
            "event_id": event_id,
            **data["body"]
        })
        return await create_visitor(result.to_model())

    @staticmethod
    async def get_user_events(user_id: int) -> UserEventSchema:
        return UserEventSchema.create(await get_visitors_events(user_id))

    @staticmethod
    async def delete_user(user_id: int, event_id: int) -> None:
        return await delete_visitor(user_id=user_id, event_id=event_id)

    @staticmethod
    async def verify(request, unique_string: str) -> dict | None:
        verify_unique_string = await verify_visitor(
            unique_string=unique_string,
        )
        if verify_unique_string is None:
            return None

        return {
            "request": request,
            "first_name": verify_unique_string.first_name,
            "last_name": verify_unique_string.last_name,
            "email": verify_unique_string.email
        }
