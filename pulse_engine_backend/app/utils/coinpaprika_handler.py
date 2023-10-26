import httpx
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every


url = "https://api.coinpaprika.com/v1"

supported_coins = (
    ("dai", "dai-dai"),
    ("usdc", "usdc-usd-coin"),
    ("usdt", "usdt-tether"),
    ("eth", "eth-ethereum"),
    ("plsx", "plsx-pulsex"),
    ("pls", "pls-pulsechain"),
    ("hex", "hex-hex"),
    ("hex-pls", "hex-hex-from-pulsechain"),
)

def coinpaprika_handler(app: FastAPI):
    @app.on_event("startup")
    @repeat_every(seconds=60)
    async def call_for_data():
        async with httpx.AsyncClient() as client:
            for symbol, ticker in supported_coins:
                r = await client.get(f"{url}/tickers/{ticker}")
                j_data = r.json()
                price = j_data['quotes']["USD"]["price"]
                print(f"price for {symbol} is {price}")