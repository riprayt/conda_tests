import asyncio
import websockets
import json

async def price_listener(symbol, url, price_data, callback):
    """
    Listens to a Binance websocket stream and updates price_data.
    Calls callback when all prices are available.
    """
    while True:
        try:
            async with websockets.connect(url) as ws:
                async for message in ws:
                    data = json.loads(message)
                    price = float(data['p'])
                    price_data[symbol] = price
                    if all(price_data.values()):
                        callback(price_data)
        except Exception as e:
            print(f"Error in {symbol} stream: {e}. reconnecting...")
            await asyncio.sleep(1)


#default stream for btcusdt
async def default_btcusdt_stream():
    price_data = {"btcusdt": None, "quantity": None}
    def print_price(data):
        print(f"BTCUSDT price: {data['btcusdt']} | quantity: {data['quantity']}")
    url = "wss://stream.binance.com:9443/ws/btcusdt@trade"
    while True:
        try:
            async with websockets.connect(url) as ws:
                async for message in ws:
                    trade = json.loads(message)
                    price_data["btcusdt"] = float(trade['p'])
                    price_data["quantity"] = float(trade['q'])
                    print_price(price_data)
        except Exception as e:
            print(f"Error in btcusdt stream: {e}. reconnecting...")
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(default_btcusdt_stream())
