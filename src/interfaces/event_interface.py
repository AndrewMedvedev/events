from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse


class EventBase(ABC):
    @abstractmethod
    async def add_event() -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def get_events() -> dict:
        raise NotImplementedError

    @abstractmethod
    async def delete_event() -> JSONResponse:
        raise NotImplementedError
