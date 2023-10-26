"""Health check."""
from fastapi import APIRouter, status
from starlette.responses import JSONResponse

health_router = APIRouter()


@health_router.get("", status_code=status.HTTP_204_NO_CONTENT)
async def health():
    """GET Request health endpoint."""
    return JSONResponse({"status": "ok"}, status_code=status.HTTP_200_OK)
