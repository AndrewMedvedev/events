import base64
import io
import logging
import os
from uuid import uuid4

from fastapi import UploadFile
from PIL import Image

from src.errors import ImageAddError, ImageGetError
from src.interfaces import ImagesBase

log = logging.getLogger(__name__)


class Images(ImagesBase):
    FOLDER = "images"

    def __init__(self) -> None:
        self.os = os

    async def add_image(
        self,
        image: UploadFile,
    ) -> str:
        log.info("Вызвана функция add_image")
        try:
            if image is not None:
                file_name = os.path.join(self.FOLDER, f"{uuid4()}{os.path.splitext(image.filename)[1]}")
                contents = await image.read()
                img = Image.open(io.BytesIO(contents))
                img.save(file_name, format="JPEG", optimize=True, quality=90)
                return file_name
            return "absent"
        except Exception as e:
            raise ImageAddError(detail=str(e))

    async def get_image(
        self,
        path: str,
    ):
        log.info("Вызвана функция get_image")
        try:
            if path != "absent":
                with open(path, "rb") as file:
                    img_bytes = file.read()
                    return base64.b64encode(img_bytes).decode("ascii")
            else:
                return "absent"
        except Exception as e:
            raise ImageGetError(detail=str(e))
