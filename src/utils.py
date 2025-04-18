from typing import Any

import base64
import io
import os
import uuid

from fastapi import UploadFile
from PIL import Image as I

from .constants import FOLDER
from .exeptions import NotFoundHTTPError


async def valid_answer(response: Any) -> dict:
    try:
        if response.status != 200:
            raise NotFoundHTTPError()
        return await response.json()
    except Exception:
        raise NotFoundHTTPError()


async def valid_image(path: str) -> bool:
    try:
        with I.open(path) as img:
            img.verify()
        return True
    except (OSError, SyntaxError, AttributeError):
        return False


class Image:
    @staticmethod
    async def add_images(image: UploadFile) -> str:
        file_name = os.path.join(FOLDER, f"{uuid.uuid4()}{os.path.splitext(image.filename)[1]}")
        contents = await image.read()
        img = I.open(io.BytesIO(contents))
        img.save(file_name, format="JPEG", optimize=True, quality=90)
        return file_name

    @staticmethod
    async def get_images(path: str):
        if path != "absent":
            with open(path, "rb") as file:
                img_bytes = file.read()
                return base64.b64encode(img_bytes).decode("ascii")
        else:
            return "absent"
