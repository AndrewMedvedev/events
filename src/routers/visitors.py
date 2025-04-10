from fastapi import APIRouter, status
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.templating import Jinja2Templates

from ..controllers import VisitorsControl

visitors = APIRouter(prefix="/api/v1/visitors", tags=["visitors"])


@visitors.post("/add/{event_id}/{user_id}")
async def add(event_id: int, user_id: int) -> Response:
    await VisitorsControl().create_user(
        user_id=user_id,
        event_id=event_id,
    )
    return Response(status_code=status.HTTP_201_CREATED)


@visitors.get("/get/{user_id}")
async def get(user_id: int) -> Response:
    result = await VisitorsControl().get_user_events(user_id=user_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=result.to_dict())


@visitors.delete("/delete/{event_id}/{user_id}")
async def delete(event_id: int, user_id: int) -> Response:
    await VisitorsControl().delete_user(user_id=user_id, event_id=event_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@visitors.get("/verify/{unique_string}", response_model=None)
async def verify_visitor(request: Request, unique_string: str) -> HTMLResponse:
    templates = Jinja2Templates(directory="templates")
    result = await VisitorsControl().verify(request=request, unique_string=unique_string)

    if result is not None:
        return templates.TemplateResponse("register.html", {"request": request, **result})

    return templates.TemplateResponse("not_register.html", {"request": request})
