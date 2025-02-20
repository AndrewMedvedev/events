from fastapi import status
from fastapi.responses import JSONResponse

from src.database.models import Event
from src.database.schemas import EventModel, EventModelUpdate
from src.database.services import CRUD


class Events:
    def __init__(self, model: EventModel = None) -> None:
        self.model = model

    async def add_event(self) -> JSONResponse:
        try:
            data = Event(
                name_event=self.model.name_event,
                date=self.model.date,
                time=self.model.time,
                location=self.model.location,
                limit_people=self.model.limit_people,
            )
            await CRUD().create_event(model=data)
            return JSONResponse(status_code=status.HTTP_200_OK,content="ok",)
        except Exception as e:
            return JSONResponse(content=e)

    async def get_events(self):
        try:
            return await CRUD().read_event()
        except Exception as e:
            return JSONResponse(content=e)

    async def update_event(self, model_id: int, values: EventModelUpdate) -> JSONResponse:
        try:
            await CRUD().update_event(
                model_id=model_id,
                values=values,
            )
            return JSONResponse(status_code=status.HTTP_200_OK,content="ok",)
        except Exception as e:
            return JSONResponse(content=e)

    async def delete_event(self, model_id: int) -> JSONResponse:
        try:
            await CRUD().delete_event(model_id=model_id)
            return JSONResponse(status_code=status.HTTP_200_OK,content="ok",)
        except Exception as e:
            return JSONResponse(content=e)
