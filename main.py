import asyncio
from arbitrage import check_arbitrage_opportunities
from stream import price_listener

price_data = {
    "btcusdt": None,
    "ethusdt": None,
    "ethbtc": None
}

async def get_prices():
    streams = {
        "btcusdt": "wss://stream.binance.com:9443/ws/btcusdt@trade",
        "ethusdt": "wss://stream.binance.com:9443/ws/ethusdt@trade",
        "ethbtc": "wss://stream.binance.com:9443/ws/ethbtc@trade"
    }
    await asyncio.gather(*(price_listener(sym, url, price_data, check_arbitrage_opportunities) for sym, url in streams.items()))

if __name__ == "__main__":
    asyncio.run(get_prices())