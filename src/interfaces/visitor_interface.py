from abc import ABC, abstractmethod

from fastapi.responses import HTMLResponse, JSONResponse


class VisitorBase(ABC):

    @abstractmethod
    async def add_user(self) -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def get_user_events(self) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    async def delete_user(self) -> JSONResponse:
        raise NotImplementedError

    @abstractmethod
    async def verify(
        self,
        unique_string: str,
    ) -> HTMLResponse:
        raise NotImplementedError
