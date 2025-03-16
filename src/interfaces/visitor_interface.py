from abc import ABC, abstractmethod

from fastapi.responses import HTMLResponse, JSONResponse


class VisitorBase(ABC):

    @abstractmethod
    async def add_user() -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def get_user_events() -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    async def delete_user() -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def verify() -> HTMLResponse:
        raise NotImplementedError
