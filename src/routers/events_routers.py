from fastapi import APIRouter

from src.classes import Events
from src.database.schemas import EventModel
from src.responses import CustomResponse

router_event = APIRouter(prefix="/api/v1/events", tags=["events"])


@router_event.post("/add/")
async def add(model: EventModel) -> CustomResponse:
    return await Events().add_event(model=model)


@router_event.get("/get/")
async def get(
    is_paginated: bool = False,
    page: int = 1,
    limit: int = 10,
) -> CustomResponse:
    return await Events().get_events(
        is_paginated=is_paginated,
        page=page,
        limit=limit,
    )


@router_event.delete("/delete/{event_id}")
async def delete(
    event_id: int,
) -> CustomResponse:
    return await Events().delete_event(model_id=event_id)
