# price_history.py
# Modified in price-history branch

import requests
import time

symbol = "BTCUSDT"
interval = "5m"
limit = 288  # 288 intervals of 5 minutes = 24 hours

url = f"https://api.binance.com/api/v3/klines"
params = {
    "symbol": symbol,
    "interval": interval,
    "limit": limit
}

response = requests.get(url, params=params)
data = response.json()

now = int(time.time() * 1000)
for candle in data:
    open_time_ms = candle[0]
    if now - open_time_ms <= 24 * 60 * 60 * 1000:
        open_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(open_time_ms / 1000))
        print(f"Time: {open_time}, Open: {candle[1]}, High: {candle[2]}, Low: {candle[3]}, Close: {candle[4]}")