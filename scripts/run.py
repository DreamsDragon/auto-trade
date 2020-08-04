"""
    Main module to run the program
"""

from autotrade.misc.datatypes import Ticker
from autotrade.market_api.nyse import NSE_MARKET_API


market_api = NYSE_MARKET_API()

a = Ticker("TTM", "Tata Motors")
market_api.get_historic_quote(a)
