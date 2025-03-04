from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse


class EventBase(ABC):

    @abstractmethod
    async def add_event(self) -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def get_events(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def delete_event(
        self,
        model_id: int,
    ) -> JSONResponse:
        raise NotImplementedError
