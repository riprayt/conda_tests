# Triangular Arbitrage Bot

This project streams live prices from Binance and checks for triangular arbitrage opportunities.

## Setup & Usage

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # for mac
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the bot:**
   ```bash
   python main.py
   ```

## Files

- `main.py`: Entrypoint.
- `arbitrage.py`: Triangular arbitrage logic.
- `stream.py`: Websocket streaming. Can also be runned independently to show btcusdt trade feed as default.

- `price_history.py`: 24h 5 min interval price fetcher.

## Requirements

- Python 3.12
- `websockets`
- `requests`
