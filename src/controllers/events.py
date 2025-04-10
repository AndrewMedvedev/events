from ..database.crud import CRUD
from ..schemas import EventListResponse, EventSchema


class EventControl:
    @staticmethod
    async def create_event(schema: EventSchema) -> None:
        return await CRUD().create_event(schema.to_model())

    @staticmethod
    async def get_event(is_paginated: bool, page: int, limit: int) -> EventListResponse:
        if not is_paginated:
            return await CRUD().read_event()
        return await CRUD().read_events_with_limit(page=page, limit=limit)

    @staticmethod
    async def delete_event(model_id: int) -> None:
        return await CRUD().delete_event(model_id=model_id)
