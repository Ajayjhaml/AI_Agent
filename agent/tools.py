from langchain_core.tools import tool
from data.market_data import get_intraday_data
from utils.indicators import add_indicators
from risk.risk_engine import (
    atr_stop_loss,
    calculate_position_size
)

import yfinance as yf
import json
from datetime import datetime


# ---------- SIGNAL LOGIC ----------
def generate_signal(rsi):
    if rsi < 35:
        return "BUY"
    elif rsi > 65:
        return "SELL"
    else:
        return "HOLD"


# ---------- OPEN INTEREST ----------
def get_open_interest(symbol):
    try:
        ticker = yf.Ticker(symbol)
        expiries = ticker.options

        if not expiries:
            return None

        nearest_expiry = expiries[0]
        chain = ticker.option_chain(nearest_expiry)

        calls_oi = chain.calls["openInterest"].sum()
        puts_oi = chain.puts["openInterest"].sum()

        return int(calls_oi + puts_oi)

    except Exception:
        return None


# ---------- LATEST NEWS ----------
def get_latest_news(symbol, limit=5):
    """
    Fetch latest news using Yahoo Finance
    """

    try:
        ticker = yf.Ticker(symbol)
        news_items = ticker.news

        if not news_items:
            return []

        formatted_news = []

        for item in news_items[:limit]:
            formatted_news.append({
                "title": item.get("title"),
                "publisher": item.get("publisher"),
                "link": item.get("link"),
                "published": datetime.fromtimestamp(
                    item.get("providerPublishTime")
                ).strftime("%Y-%m-%d %H:%M:%S")
            })

        return formatted_news

    except Exception:
        return []


# ---------- MAIN TOOL ----------
@tool
def analyze_symbol(symbol: str) -> str:
    """
    Analyze stock and return:
    - Price data
    - Risk management
    - Signal
    - Open Interest
    - Latest news
    """

    # Get price data
    df = get_intraday_data(symbol)
    df = add_indicators(df)

    latest = df.iloc[-1]

    entry = float(latest["close"])
    atr = float(latest["atr"])
    rsi = float(latest["rsi"])

    stop = float(atr_stop_loss(entry, atr))
    size = float(calculate_position_size(entry, stop))

    signal = generate_signal(rsi)
    oi = get_open_interest(symbol)
    news = get_latest_news(symbol)

    result = {
        "symbol": symbol,
        "analysis_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "market_data": {
            "entry_price": round(entry, 2),
            "atr": round(atr, 2),
            "rsi": round(rsi, 2),
            "open_interest": oi
        },
        "risk_management": {
            "suggested_stop_loss": round(stop, 2),
            "position_size": round(size, 2),
        },
        "signal": signal,
        "latest_news": news
    }

    return json.dumps(result, indent=4)
