"""Init file for routers."""
from .health import health_router
from .basic_metrics import basic_metrics_router


__all__ = [
    "health_router",
    "basic_metrics_router",
]
