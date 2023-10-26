"""Basic metrics router."""
from fastapi import APIRouter, status

router = APIRouter()

@router.get("")
async def get_basic_metrics():
    """GET basic metrics.

    Returns:
        Basic metrics object

    Raises:
        HTTPException - if ValidationError
    """
    data = _get_basic_metrics()
    return data

def _get_basic_metrics():
    return {
        "prices": {
            "dai": 1.0,
            "usdc": 1.0,
            "usdt": 1.0,
            "eth": 1700.2,
            "plsx": 0.0004,
            "pls": 0.00004,
            "hex": 0.03,
            "hex-pls": 0.004,
        },
        "network": {
            "block_number": 184759,
        }
    }
