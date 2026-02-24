# import os
# from dotenv import load_dotenv

# load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

# ACCOUNT_BALANCE = 10000
# RISK_PER_TRADE = 0.02

import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
KITE_API_KEY = os.getenv("KITE_API_KEY")
KITE_API_SECRET = os.getenv("KITE_API_SECRET")
KITE_ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

ACCOUNT_BALANCE = 100000  # Total capital
RISK_PER_TRADE = 0.02     # 2% per trade
TRAILING_STOP_MULTIPLIER = 1.2