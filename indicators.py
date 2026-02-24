import ta

def add_indicators(df):
    df["atr"] = ta.volatility.AverageTrueRange(
        df["high"], df["low"], df["close"], window=14
    ).average_true_range()

    df["rsi"] = ta.momentum.RSIIndicator(
        df["close"], window=14
    ).rsi()

    return df