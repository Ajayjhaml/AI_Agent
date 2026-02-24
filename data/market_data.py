import yfinance as yf
import pandas as pd


def get_intraday_data(symbol="AAPL", interval="5m", period="5d"):
    """
    Fetch intraday data using Yahoo Finance (no API key required)
    """

    ticker = yf.Ticker(symbol)
    df = ticker.history(interval=interval, period=period)

    if df.empty:
        raise Exception("Invalid symbol or no data available")

    df = df.rename(columns={
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume"
    })

    df = df[["open", "high", "low", "close", "volume"]]

    return df
