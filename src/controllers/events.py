from ..database.crud import SQLEvent
from ..schemas import EventListResponse, EventSchema


class EventControl:
    def __init__(self):
        self.sql_event = SQLEvent()

    async def create_event(self, schema: EventSchema) -> None:
        return await self.sql_event.create_events(schema.to_model())

    async def get_event(self, is_paginated: bool, page: int, limit: int) -> EventListResponse:
        if not is_paginated:
            return await self.sql_event.read_events()
        return await self.sql_event.read_events_with_limit(page=page, limit=limit)

    async def delete_event(self, model_id: int) -> None:
        return await self.sql_event.delete_events(model_id=model_id)
