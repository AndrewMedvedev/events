from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse

from ..controllers import EventControl
from ..schemas import EventSchema

events = APIRouter(prefix="/api/v1/events", tags=["events"])


@events.post("/add/")
async def add(schema: EventSchema) -> Response:
    await EventControl().create_event(schema)
    return Response(status_code=status.HTTP_201_CREATED)


@events.get("/get/")
async def get(is_paginated: bool = False, page: int = 1, limit: int = 10) -> Response:
    result = await EventControl().get_event(is_paginated, page, limit)
    return JSONResponse(status_code=status.HTTP_200_OK, content=result.to_dict())


@events.delete("/delete/{event_id}")
async def delete(event_id: int) -> Response:
    await EventControl().delete_event(model_id=event_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
