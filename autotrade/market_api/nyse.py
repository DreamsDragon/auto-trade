"""
    Market API for NSE
"""
import os
import urllib.request


from . import AbstractMarketAPI
from ..misc.datatypes import Ticker, Time


def probe_nyse(ticker_symbol: str, interval=1):
    key = os.environ["ALPHA_VANTAGE_KEY"]
    if interval > 60:
        interval = 60
    if interval < 1:
        interval = 1
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval={1}min&apikey={2}".format(
        ticker_symbol, interval, key
    )
    req = urllib.request.Request(url, headers={"User-Agent": "Chrome Browser"})
    fp = urllib.request.urlopen(req, timeout=100)
    mybytes = fp.read()

    return mystr


class NYSE_MARKET_API(AbstractMarketAPI):
    def __init__(self):
        pass

    def get_quote(self, ticker: Ticker):
        """
            Get the live quote of a ticker
        """
        pass

    def get_historic_quote(
        self, ticker: Ticker, start: Time = None, end: Time = None, interval: int = 1
    ):
        """
            Get historic quotes in the time period
        """
        print(probe_nse(ticker.symbol, interval))

    def get_all_stocks(self):
        """
            Return list of all available stocks
        """
        pass
