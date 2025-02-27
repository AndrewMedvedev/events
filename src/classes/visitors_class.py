from fastapi import status
from fastapi.responses import JSONResponse
import uuid
import segno


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
        user_model_visitor = Visitor(
            user_id=self.user_id,
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            event_id=self.event_id,
            unique_string=str(uuid.uuid4()),
        )
        await CRUD().create_visitor(user_model_visitor)
        return JSONResponse(
            content=status.HTTP_200_OK,
        )

    async def get_user_events(self) -> list[dict]:
        events = await CRUD().get_visitors_events(
            user_id=self.user_id,
        )
        return [
            {
                "event_id": i.event_id,
                "unique_string": i.unique_string,
            }
            for i in events
        ]

    async def delete_user(self) -> JSONResponse:
        await CRUD().delete_visitor(
            user_id=self.user_id,
            event_id=self.event_id,
        )
        return JSONResponse(
            content=status.HTTP_200_OK,
        )

    @staticmethod
    async def verify(unique_string: str) -> JSONResponse:
        obj = await CRUD().verify_visitor(
            unique_string=unique_string,
        )
        if obj != None:
            return JSONResponse(content="Зарегестрирован")
        else:
            return JSONResponse(content="Не зарегестрирован")
        

    async def make_qr(self):
        unique = await CRUD().get_visitor_unique_string(user_id=self.user_id, event_id=self.event_id)
        qr = segno.make_qr(f"https://events-fastapi.onrender.com/api/v1/visitors/verify/{unique}")
        return qr.show()
