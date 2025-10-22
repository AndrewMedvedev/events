from collections.abc import Sequence
from uuid import UUID

from dishka.integrations.fastapi import DishkaRoute
from dishka.integrations.fastapi import FromDishka as Depends
from fastapi import APIRouter, status
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from ...core.domain import VisitorSchema
from ...services.visitors import VisitorService

visitors = APIRouter(route_class=DishkaRoute, prefix="/visitors", tags=["visitors"])


@visitors.post("/{event_id}/{user_id}", status_code=status.HTTP_201_CREATED)
async def add(service: Depends[VisitorService], event_id: int, user_id: UUID) -> None:
    await service.create_user(
        user_id=user_id,
        event_id=event_id,
    )


@visitors.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get(service: Depends[VisitorService], user_id: UUID) -> Sequence[VisitorSchema]:
    return await service.get_user_events(user_id=user_id)


@visitors.delete("/{event_id}/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(service: Depends[VisitorService], event_id: int, user_id: UUID) -> None:
    await service.delete_user(user_id=user_id, event_id=event_id)


@visitors.get("/verify/{unique_string}", response_model=None)
async def verify_visitor(
    service: Depends[VisitorService],
    request: Request,
    unique_string: str,
) -> HTMLResponse:
    templates = Jinja2Templates(directory="templates")
    result = await service.verify(request=request, unique_string=unique_string)

    if result is not None:
        return templates.TemplateResponse("register.html", {"request": request, **result})

    return templates.TemplateResponse("not_register.html", {"request": request})


@visitors.get("/make/qr/{unique_string}")
async def make_qr(unique_string: str, service: Depends[VisitorService]) -> StreamingResponse:
    return await service.make_qr(unique_string=unique_string)
