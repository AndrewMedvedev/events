from typing import Any

import logging

import aiohttp
from PIL import Image

from src.config import Settings
from src.errors.errors import SendError

log = logging.getLogger(__name__)


async def get_user_data(user_id: int) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url=f"{Settings.GET_DATA}{user_id}",
            ssl=False,
        ) as data:
            return await valid_answer(response=data, name_func="get_user_data")


async def valid_answer(
    response: Any,
    name_func: str,
) -> dict:
    try:
        log.warning(await response.text())
        if response.status == 200:
            data_dict = await response.json()
            log.warning(data_dict)
            return data_dict
        raise SendError(name_func)
    except Exception:
        raise SendError(name_func)


async def valid_image(path: str) -> bool:
    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except (OSError, SyntaxError):
        return False


def config_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )
