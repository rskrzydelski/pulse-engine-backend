"""Main app."""
import uvicorn
from fastapi import FastAPI

from pulse_engine_backend.app.api.api import api_router
from pulse_engine_backend.app.core.config import settings


def create_app() -> FastAPI:
    """Create FastAPI app."""
    app_fastapi = FastAPI(title=settings.PROJECT_NAME)

    app_fastapi.include_router(api_router, prefix=settings.API_STR)
    return app_fastapi


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host=settings.UVICORN_ADDRESS_MAIN, port=settings.UVICORN_PORT_MAIN)
