from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.classes import Events
from src.database.schemas import EventModel

router_event = APIRouter(prefix="/api/v1/events", tags=["events"])


@router_event.post("/add/")
async def add(model: EventModel) -> JSONResponse:
    return await Events().add_event(model=model)


@router_event.get("/get/")
async def get() -> JSONResponse:
    return await Events().get_events()


@router_event.delete("/delete/{event_id}")
async def delete(
    event_id: int,
) -> JSONResponse:
    return await Events().delete_event(model_id=event_id)
