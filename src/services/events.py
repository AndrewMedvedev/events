from ..core.domain import EventSchema
from ..database.repository import EventRepository


class EventService:
    def __init__(self, repository: EventRepository) -> None:
        self.repository = repository

    async def create_event(self, schema: EventSchema) -> EventSchema:
        return await self.repository.create(schema)

    async def get_event(self, page: int, limit: int) -> list[EventSchema]:
        return await self.repository.read_all(limit, page)

    async def delete_event(self, model_id: int) -> bool:
        return await self.repository.delete(model_id)
