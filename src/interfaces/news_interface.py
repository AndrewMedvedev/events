from abc import ABC, abstractmethod


class NewsBase(ABC):
    @abstractmethod
    async def add_news():
        raise NotImplementedError

    @abstractmethod
    async def get_news():
        raise NotImplementedError

    @abstractmethod
    async def delete_news():
        raise NotImplementedError
