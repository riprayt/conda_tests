def check_arbitrage_opportunities(price_data):
    """
    Checks for triangular arbitrage opportunities given price data.
    """
    btc_usdt = price_data["btcusdt"]
    eth_usdt = price_data["ethusdt"]
    eth_btc = price_data["ethbtc"]

    print("\narbitrage possibilities:")
    paths = [
        ("usdt", "btc", "eth", lambda: (1 / btc_usdt) * (1/eth_btc) * eth_usdt),
        ("usdt", "eth", "btc", lambda: (1 / eth_usdt) * eth_btc * btc_usdt),
        ("btc", "usdt", "eth", lambda: btc_usdt * (1 / eth_usdt) * (eth_btc)),
        ("btc", "eth", "usdt", lambda: (1/eth_btc) * eth_usdt * (1 / btc_usdt)),
        ("eth", "usdt", "btc", lambda: eth_usdt * (1 / btc_usdt) * (1 / eth_btc)),
        ("eth", "btc", "usdt", lambda: (eth_btc) * btc_usdt * (1 / eth_usdt))
    ]
    for a, b, c, calc in paths:
        try:
            profit = calc()
            percent_profit = (profit - 1) * 100
            if percent_profit > 0.1: 
                print(f"✅ arbitrage found ({a}->{b}->{c}->{a}): {percent_profit:.2f}% profit")
            else:
                print(f"({a}->{b}->{c}->{a}): {percent_profit:.2f}% profit")
        except Exception as e:
            print(f"Error calculating path {a}->{b}->{c}->{a}: {e}")
