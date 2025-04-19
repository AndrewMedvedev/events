from typing import Any

import base64
import io
import os
import uuid

import anyio
from fastapi import UploadFile
from PIL import Image

from .constants import FOLDER, STATUS_OK
from .exeptions import NotFoundHTTPError


async def valid_answer(response: Any) -> dict:
    if response.status != STATUS_OK:
        raise NotFoundHTTPError
    return await response.json()


def valid_image(path: str) -> bool:
    try:
        with Image.open(path) as img:
            img.verify()
    except (OSError, SyntaxError, AttributeError):
        return False
    else:
        return True


class Images:
    @staticmethod
    async def add_images(image: UploadFile) -> str:
        file_name = os.path.join(FOLDER, f"{uuid.uuid4()}{os.path.splitext(image.filename)[1]}")
        contents = await image.read()
        img = Image.open(io.BytesIO(contents))
        img.save(file_name, format="JPEG", optimize=True, quality=90)
        return file_name

    @staticmethod
    async def get_images(path: str):
        if path != "absent":
            async with await anyio.open_file(path, "rb") as file:
                img_bytes = file.read()
                return base64.b64encode(img_bytes).decode("ascii")
        else:
            return "absent"
