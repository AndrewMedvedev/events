from dishka.integrations.fastapi import DishkaRoute
from dishka.integrations.fastapi import FromDishka as Depends
from fastapi import APIRouter, status

from ...core.domain import EventSchema
from ...services.events import EventService

events = APIRouter(route_class=DishkaRoute, prefix="/events", tags=["events"])


@events.post("/", status_code=status.HTTP_201_CREATED, response_model=EventSchema)
async def add(schema: EventSchema, service: Depends[EventService]) -> EventSchema:
    return await service.create_event(schema)


@events.get("/", status_code=status.HTTP_200_OK)
async def get(service: Depends[EventService], page: int = 1, limit: int = 10) -> list[EventSchema]:
    return await service.get_event(page, limit)


@events.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(service: Depends[EventService], event_id: int) -> None:
    await service.delete_event(model_id=event_id)
