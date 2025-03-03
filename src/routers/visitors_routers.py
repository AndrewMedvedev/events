from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse

from src.classes import Visitors

router_visitors = APIRouter(prefix="/api/v1/visitors", tags=["visitors"])


@router_visitors.post("/add/{event_id}/{user_id}")
async def add(
    event_id: int,
    user_id: int,
) -> JSONResponse:
    try:
        return await Visitors(
            user_id=user_id,
            event_id=event_id,
        ).add_user()
    except Exception as e:
        return JSONResponse(
            content={"detail": str(e)},
        )


@router_visitors.get("/get/{user_id}")
async def get(user_id: int) -> JSONResponse:
    try:
        return await Visitors(user_id=user_id).get_user_events()
    except Exception as e:
        return JSONResponse(
            content={"detail": str(e)},
        )


@router_visitors.delete("/delete/{event_id}/{user_id}")
async def delete(
    event_id: int,
    user_id: int,
) -> JSONResponse:
    try:
        return await Visitors(
            user_id=user_id,
            event_id=event_id,
        ).delete_user()
    except Exception as e:
        return JSONResponse(
            content={"detail": str(e)},
        )


@router_visitors.get(
    "/verify/{unique_string}",
    response_model=None,
)
async def verify_visitor(unique_string: str) -> HTMLResponse | JSONResponse:
    try:
        return await Visitors().verify(
            unique_string=unique_string,
        )
    except Exception as e:
        return JSONResponse(
            content={"detail": str(e)},
        )
