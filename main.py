from src.api.app import create_fastapi_app, setup_errors_handlers, setup_middleware

app = create_fastapi_app()
setup_middleware(app)
setup_errors_handlers(app)
