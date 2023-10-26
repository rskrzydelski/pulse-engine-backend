"""API definition."""
from fastapi import APIRouter

from .routers.health import health_router
from .routers import basic_metrics_router


api_router = APIRouter()
api_router.include_router(health_router, prefix="/health", tags=["health"])
api_router.include_router(basic_metrics_router, prefix="/basic_metrics", tags=["metrics"])
