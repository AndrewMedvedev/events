import logging

from fastapi import status

from src.database.models import Event
from src.database.schemas import EventModel
from src.database.services import CRUDEvents
from src.interfaces import EventBase
from src.responses import CustomResponse

log = logging.getLogger(__name__)


class Events(EventBase):

    def __init__(self) -> None:
        self.crud = CRUDEvents()
        self.event = Event

    async def add_event(
        self,
        model: EventModel,
    ) -> CustomResponse:
        log.info("Вызвана функция add_event")
        data = self.event(
            name_event=model.name_event,
            date_time=model.date_time,
            location=model.location,
            description=model.description,
            limit_people=model.limit_people,
            points_for_the_event=model.points_for_the_event,
        )
        return CustomResponse(
            status_code=status.HTTP_201_CREATED,
            body=await self.crud.create_event(model=data),
        )

    async def get_events(
        self,
        is_paginated: bool,
        page: int,
        limit: int,
    ) -> CustomResponse:
        log.info("Вызвана функция get_events")
        if is_paginated:
            return CustomResponse(
                status_code=status.HTTP_200_OK,
                body=await self.crud.read_events_with_limit(
                    page=page,
                    limit=limit,
                ),
            )
        return CustomResponse(
            status_code=status.HTTP_200_OK,
            body=await self.crud.read_event(),
        )

    async def delete_event(
        self,
        model_id: int,
    ) -> CustomResponse:
        log.info("Вызвана функция delete_event")
        return CustomResponse(
            status_code=status.HTTP_204_NO_CONTENT,
            body=await self.crud.delete_event(model_id=model_id),
        )
