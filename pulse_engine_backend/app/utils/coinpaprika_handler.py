import httpx
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
import redis
from .constans import supported_coins


url = "https://api.coinpaprika.com/v1"

rd = redis.Redis(host="localhost", port=6379, db=0)


def coinpaprika_handler(app: FastAPI):
    @app.on_event("startup")
    @repeat_every(seconds=60)
    async def call_for_data():
        async with httpx.AsyncClient() as client:
            for symbol, ticker in supported_coins:
                r = await client.get(f"{url}/tickers/{ticker}")
                j_data = r.json()
                price = j_data['quotes']["USD"]["price"]
                rd.set(symbol, price)
