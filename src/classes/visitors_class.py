from fastapi import status
from fastapi.responses import JSONResponse


from src.database import get_data
from src.database.models import Visitor
from src.database.services.crud import CRUD


class Visitors:

    def __init__(
        self,
        user_id: int,
        event_id: int = None,
    ) -> None:
        self.user_id = user_id
        self.event_id = event_id

    async def add_user(self) -> JSONResponse:
        data = await get_data(
            self.user_id,
        )
        user_model = Visitor(
            user_id=self.user_id,
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            event_id=self.event_id,
        )
        await CRUD().create_visitor(user_model)

        return JSONResponse(
            content=status.HTTP_200_OK,
        )

    async def get_user_events(self) -> list[dict]:
        events = await CRUD().get_visitors_events(
            user_id=self.user_id,
        )
        return [{"event_id": i.event_id} for i in events]

    async def delete_user(self) -> JSONResponse:
        await CRUD().delete_visitor(
            user_id=self.user_id,
            event_id=self.event_id,
        )
        return JSONResponse(
            content=status.HTTP_200_OK,
        )
