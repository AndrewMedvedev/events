import uvicorn

from src.api.app import create_fastapi_app, setup_errors_handlers, setup_middleware

app = create_fastapi_app()
setup_middleware(app)
setup_errors_handlers(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)  # noqa: S104
