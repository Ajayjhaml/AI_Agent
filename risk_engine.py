# from config import ACCOUNT_BALANCE, RISK_PER_TRADE

# def calculate_position_size(entry_price, stop_price):
#     risk_amount = ACCOUNT_BALANCE * RISK_PER_TRADE
#     risk_per_share = abs(entry_price - stop_price)

#     if risk_per_share == 0:
#         return 0

#     position_size = risk_amount / risk_per_share
#     return round(position_size, 2)


# def atr_stop_loss(entry_price, atr, multiplier=1.5):
#     return entry_price - (atr * multiplier)


# def trailing_stop(highest_price, atr, multiplier=1.2):
#     return highest_price - (atr * multiplier)

from config import ACCOUNT_BALANCE, RISK_PER_TRADE, TRAILING_STOP_MULTIPLIER

def calculate_position_size(entry_price, stop_price):
    risk_amount = ACCOUNT_BALANCE * RISK_PER_TRADE
    risk_per_share = abs(entry_price - stop_price)
    if risk_per_share == 0:
        return 0
    return round(risk_amount / risk_per_share)

def atr_stop_loss(entry_price, atr, multiplier=1.5):
    return entry_price - (atr * multiplier)

def trailing_stop(highest_price, atr):
    return highest_price - (atr * TRAILING_STOP_MULTIPLIER)