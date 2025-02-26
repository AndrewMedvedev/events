from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse

from src.classes import Visitors

router_visitors = APIRouter(prefix="/api/v1/visitors", tags=["visitors"])


@router_visitors.post("/add/{event_id}")
async def add(event_id: int, request: Request, response: Response) -> JSONResponse:
    try:
        access = request.cookies.get("access")
        refresh = request.cookies.get("refresh")
        return await Visitors(
            token_access=access,
            token_refresh=refresh,
            event_id=event_id,
            response=response,
        ).add_user()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(e)},
        )


@router_visitors.get("/get")
async def get(request: Request, response: Response) -> JSONResponse:
    try:
        access = request.cookies.get("access")
        refresh = request.cookies.get("refresh")
        return await Visitors(
            token_access=access,
            token_refresh=refresh,
            response=response,
        ).get_user_events()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(e)},
        )


@router_visitors.delete("/delete/{event_id}")
async def delete(event_id: int, request: Request, response: Response) -> JSONResponse:
    try:
        access = request.cookies.get("access")
        refresh = request.cookies.get("refresh")
        return await Visitors(
            token_access=access,
            token_refresh=refresh,
            event_id=event_id,
            response=response,
        ).delete_user()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(e)},
        )
