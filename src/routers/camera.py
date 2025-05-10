from base64 import decode

import cv2
from fastapi import APIRouter, HTTPException

camera = APIRouter(tags=["camera"])


@camera.get("/scan-from-camera")
async def scan_from_camera():
    """
    Сканирование QR-кода с веб-камеры
    """
    cap = cv2.VideoCapture(0)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                raise HTTPException(
                    status_code=500, detail="Не удалось получить изображение с камеры"
                )

            decoded_objects = decode(frame)

            if decoded_objects:
                cap.release()
                data = decoded_objects[0].data.decode("utf-8")
                return {"status": "success", "data": data}

            # Для демонстрации можно добавить задержку
            # и ограничить количество попыток в реальном приложении

    finally:
        cap.release()
