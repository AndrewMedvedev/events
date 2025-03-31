from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse

from src.classes import Visitors
from src.responses import CustomResponse

router_visitors = APIRouter(prefix="/api/v1/visitors", tags=["visitors"])


@router_visitors.post("/add/{event_id}/{user_id}")
async def add(
    event_id: int,
    user_id: int,
) -> CustomResponse:
    return await Visitors().add_user(
        user_id=user_id,
        event_id=event_id,
    )


@router_visitors.get("/get/{user_id}")
async def get(user_id: int) -> CustomResponse:
    return await Visitors().get_user_events(user_id=user_id)


@router_visitors.delete("/delete/{event_id}/{user_id}")
async def delete(
    event_id: int,
    user_id: int,
) -> CustomResponse:
    return await Visitors().delete_user(
        user_id=user_id,
        event_id=event_id,
    )


@router_visitors.get(
    "/verify/{unique_string}",
    response_model=None,
)
async def verify_visitor(unique_string: str) -> HTMLResponse | JSONResponse:
    return await Visitors().verify(
        unique_string=unique_string,
    )
