from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.classes import Events
from src.database.schemas import EventModel, EventModelUpdate

router_event = APIRouter(prefix="/event", tags=["event"])


@router_event.post("/v1/add/")
async def add(model: EventModel) -> JSONResponse:
    try:
        return await Events(model=model).add_event()
    except Exception as e:
        return JSONResponse(content=e)


@router_event.get("/v1/get/")
async def get() -> JSONResponse:
    try:
        return await Events().get_events()
    except Exception as e:
        return JSONResponse(content=e)


@router_event.put("/v1/update/{model_id}")
async def update(model: EventModelUpdate, model_id: int) -> JSONResponse:
    try:
        return await Events().update_event(
            model_id=model_id,
            values=model,
        )
    except Exception as e:
        return JSONResponse(content=e)


@router_event.delete("/v1/delete/{model_id}")
async def delete(
    model_id: int,
) -> JSONResponse:
    try:
        return await Events().delete_event(model_id=model_id)
    except Exception as e:
        return JSONResponse(content=e)
