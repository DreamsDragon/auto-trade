"""
    Main module to run the program
"""

from autotrade.misc.datatypes import Ticker
from autotrade.market_api.nyse import NYSE_MARKET_API

listing_path = "./data/nasdaq.txt"

market_api = NYSE_MARKET_API(listing_path, "|")

all_tickers = market_api.get_all_stocks()

a = Ticker("TTM", "Tata Motors")
historic_data = market_api.get_historic_quote(a)
print(market_api.get_quote(a))
print(len(market_api.get_all_stocks()))
