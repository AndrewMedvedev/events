from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.classes import Events
from src.database.schemas import EventModel

router_event = APIRouter(prefix="/api/v1/events", tags=["events"])


@router_event.post("/add/")
async def add(model: EventModel) -> JSONResponse:
    try:
        return await Events(model=model).add_event()
    except Exception:
        return JSONResponse(content=str(Exception), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router_event.get("/get/")
async def get() -> JSONResponse:
    try:
        return await Events().get_events()
    except Exception:
        return JSONResponse(content=str(Exception), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @router_event.put("/update/{model_id}")
# async def update(model: EventModelUpdate, model_id: int) -> JSONResponse:
#     try:
#         return await Events().update_event(
#             model_id=model_id,
#             values=model,
#         )
#     except Exception:
#         return JSONResponse(content=str(Exception), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router_event.delete("/delete/{event_id}")
async def delete(
    event_id: int,
) -> JSONResponse:
    try:
        return await Events().delete_event(model_id=event_id)
    except Exception:
        return JSONResponse(content=str(Exception), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
