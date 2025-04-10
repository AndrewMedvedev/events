import base64
import io
import os
import uuid

from fastapi import UploadFile
from PIL import Image as I

from ..constants import FOLDER


class Image:
    @staticmethod
    async def add_image(image: UploadFile) -> str:
        dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), FOLDER)
        file_name = os.path.join(FOLDER, f"{uuid.uuid4()}{os.path.splitext(image.filename)[1]}")
        contents = await image.read()
        img = I.open(io.BytesIO(contents))
        img.save(file_name, format="JPEG", optimize=True, quality=90)
        return file_name

    @staticmethod
    async def get_image(path: str):
        if path != "absent":
            with open(path, "rb") as file:
                img_bytes = file.read()
                return base64.b64encode(img_bytes).decode("ascii")
        else:
            return "absent"
        
