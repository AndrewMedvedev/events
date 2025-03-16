from abc import ABC, abstractmethod



class CRUDEventBase(ABC):

    @abstractmethod
    async def create_event() -> dict:
        raise NotImplementedError

    @abstractmethod
    async def read_event() -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    async def update_event() -> dict:
        raise NotImplementedError

    @abstractmethod
    async def delete_event() -> dict | str:
        raise NotImplementedError


class CRUDVisitorBase(ABC):

    @abstractmethod
    async def create_visitor() -> dict:
        raise NotImplementedError

    @abstractmethod
    async def get_visitors_events() -> dict | str:
        raise NotImplementedError

    @abstractmethod
    async def delete_visitor() -> dict | str:
        raise NotImplementedError

    @abstractmethod
    async def verify_visitor() -> str:
        raise NotImplementedError
