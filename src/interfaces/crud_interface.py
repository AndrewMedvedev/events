from abc import ABC, abstractmethod

from pydantic import BaseModel
from src.database.models import Event, Visitor


class CRUDEventBase(ABC):

    @abstractmethod
    async def create_event(
        self,
        model: Event,
    ) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def read_event(self) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    async def update_event(
        self,
        event_id: int,
        values: BaseModel,
    ) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def delete_event(
        self,
        model_id: int,
    ) -> dict | str:
        raise NotImplementedError


class CRUDVisitorBase(ABC):

    @abstractmethod
    async def create_visitor(
        self,
        model: Visitor,
    ) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def get_visitors_events(
        self,
        user_id: int,
    ) -> dict | str:
        raise NotImplementedError

    @abstractmethod
    async def delete_visitor(
        self,
        user_id: int,
        event_id: int,
    ) -> dict | str:
        raise NotImplementedError

    @abstractmethod
    async def verify_visitor(self, unique_string: str) -> str:
        raise NotImplementedError
