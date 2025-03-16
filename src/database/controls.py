import logging
from venv import logger

import aiohttp

from src.config import Settings
from src.errors.errors import SendError


async def get_user_data(user_id: int) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url=f"{Settings.GET_DATA}{user_id}",
            ssl=False,
        ) as data:
            try:
                user_data = await data.json()
                logger.warning(user_data)
                if "email" in user_data:
                    return user_data
                raise SendError("get_user_data")
            except SendError:
                raise SendError("get_user_data")


def config_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )
