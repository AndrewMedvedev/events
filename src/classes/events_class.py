import logging
from fastapi.responses import JSONResponse

from src.database.models import Event
from src.database.schemas import EventModel
from src.database.services import CRUD
from src.interfaces import EventBase
from src.database import config_logging


class Events(EventBase):

    config_logging(level=logging.WARNING)

    def __init__(self) -> None:
        self.crud = CRUD()
        self.event = Event

    async def add_event(
        self,
        model: EventModel,
    ) -> JSONResponse:
        data = self.event(
            name_event=model.name_event,
            date_time=model.date_time,
            location=model.location,
            description=model.description,
            limit_people=model.limit_people,
            points_for_the_event=model.points_for_the_event,
        )
        return JSONResponse(
            content=await self.crud.create_event(model=data),
        )

    async def get_events(self) -> dict:
        return await self.crud.read_event()

    # async def update_event(
    #     self,
    #     model_id: int,
    #     values: EventModelUpdate,
    # ) -> JSONResponse:
    #     try:
    #         await CRUD().update_event(
    #             model_id=model_id,
    #             values=values,
    #         )
    #         return JSONResponse(content=status.HTTP_200_OK)
    #     except Exception as e:
    #         return JSONResponse(content=e)

    async def delete_event(
        self,
        model_id: int,
    ) -> JSONResponse:
        return JSONResponse(
            content=await self.crud.delete_event(model_id=model_id),
        )
