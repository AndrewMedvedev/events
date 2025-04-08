from typing import Any

from PIL import Image

from .exceptions import SendError


async def valid_answer(response: Any, name_func: str) -> dict:
    try:
        if response.status != 200:
            raise SendError(name_func)
        data_dict = await response.json()
        return data_dict
    except Exception:
        raise SendError(name_func)


async def valid_image(path: str) -> bool:
    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except (OSError, SyntaxError):
        return False
