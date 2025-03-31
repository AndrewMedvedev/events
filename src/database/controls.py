import logging
import os
from typing import Any
from uuid import uuid4

import aiohttp
from fastapi import UploadFile

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
        else:
            raise SendError(name_func)
    except Exception:
        raise SendError(name_func)


async def add_image(
    self,
    image: UploadFile,
) -> dict:
    if image is not None:
        file_ext = os.path.splitext(image.filename)[1]  # получаем расширение файла
        file_path = os.path.join(self.IMAGE_FOLDER, f"{uuid4()}{file_ext}")
        with open(file_path, "wb") as buffer:
            buffer.write(await image.read())
        return file_path
    return "absent"


def config_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )
