from abc import ABC, abstractmethod


class CRUDEventBase(ABC):
    @abstractmethod
    async def create_event():
        raise NotImplementedError

    @abstractmethod
    async def read_event():
        raise NotImplementedError

    @abstractmethod
    async def delete_event():
        raise NotImplementedError


class CRUDVisitorBase(ABC):
    @abstractmethod
    async def create_visitor():
        raise NotImplementedError

    @abstractmethod
    async def get_visitors_events():
        raise NotImplementedError

    @abstractmethod
    async def delete_visitor():
        raise NotImplementedError

    @abstractmethod
    async def verify_visitor():
        raise NotImplementedError


class CRUDNewsBase(ABC):
    @abstractmethod
    async def add_news():
        raise NotImplementedError

    @abstractmethod
    async def read_news():
        raise NotImplementedError

    @abstractmethod
    async def delete_news():
        raise NotImplementedError
