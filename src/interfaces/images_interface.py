from abc import ABC, abstractmethod


class ImagesBase(ABC):
    @abstractmethod
    async def add_image():
        raise NotImplementedError

    @abstractmethod
    async def get_image():
        raise NotImplementedError
