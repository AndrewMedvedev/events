from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.database.models import Event
from src.database.services.orm import DatabaseSessionService


class CRUD(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_event(
        self,
        model: Event,
    ) -> JSONResponse:
        async with self.session() as session:
            session.add(model)
            await session.commit()
            await session.refresh(model)
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message": 200})

    async def read_event(self) -> dict:
        async with self.session() as session:
            events = await session.execute(select(Event))
        try:
            return events.scalars().all()
        except Exception as _ex:
            print(_ex)

    async def update_event(
        self,
        model_id: int,
        values: BaseModel,
    ) -> JSONResponse:
        async with self.session() as session:
            values_dict = values.model_dump(exclude_unset=True)
            try:
                stmt = await session.execute(select(Event).where(Event.id == model_id))
                stmt = stmt.scalar()
                for key, value in values_dict.items():
                    if value != "string":
                        setattr(stmt, key, value)
                    else:
                        continue
                await session.commit()
                return JSONResponse(status_code=status.HTTP_200_OK,content={"message": 200})
            except SQLAlchemyError as e:
                print(e)
                return JSONResponse(content=e)

    async def delete_event(
        self,
        model_id: int,
    ) -> JSONResponse:
        async with self.session() as session:
            obj = await session.get(Event, model_id)
            try:
                if obj:
                    await session.delete(obj)
                    await session.commit()
                    return JSONResponse(status_code=status.HTTP_200_OK,content={"message": 200})
            except Exception as e:
                print(e)
                return JSONResponse(content=e)
