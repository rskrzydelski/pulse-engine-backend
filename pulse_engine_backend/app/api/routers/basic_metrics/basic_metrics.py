"""Basic metrics router."""
from fastapi import APIRouter
import redis

from pulse_engine_backend.app.utils.constans import supported_coins

router = APIRouter()

rd = redis.Redis(host="localhost", port=6379, db=0)


@router.get("")
async def get_basic_metrics():
    """GET basic metrics.

    Returns:
        Basic metrics object

    Raises:
        HTTPException - if ValidationError
    """
    data = {}
    for symbol, _ in supported_coins:
        cache = rd.get(symbol)
        if cache is None:
            continue
        data[symbol] = cache
    return data
