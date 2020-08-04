"""
    Market API for NSE
"""
import os
import urllib.request
from json import loads
from datetime import datetime

from . import AbstractMarketAPI
from ..misc.datatypes import Ticker, Time, Quote, Price


def probe_nyse(url: str):

    req = urllib.request.Request(url, headers={"User-Agent": "Chrome Browser"})
    fp = urllib.request.urlopen(req, timeout=100)
    mybytes = fp.read()
    data = loads(mybytes)
    return data


class NYSE_MARKET_API(AbstractMarketAPI):
    def __init__(
        self, listing_file=None, listing_file_delimiter=None,
    ):
        self.key = os.environ["ALPHA_VANTAGE_KEY"]
        self.all_tickers = {}
        if (listing_file != None) and (listing_file_delimiter != None):
            self._read_listing(listing_file, listing_file_delimiter)

    def _read_listing(self, listing_file, listing_file_delimiter):
        with open(listing_file) as f:
            for line in f:
                split_line = line.split(listing_file_delimiter)
                symbol = split_line[0]
                name = split_line[1]
                self.all_tickers[name] = Ticker(symbol, name)

    def get_quote(self, ticker: Ticker):
        """
            Get the live quote of a ticker
        """
        url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={0}&outputsize=compact&apikey={1}".format(
            ticker.symbol, self.key
        )
        data = probe_nyse(url)["Global Quote"]
        quote = Quote(
            ticker,
            datetime.now(),
            Price(data["02. open"]),
            Price(data["03. high"]),
            Price(data["04. low"]),
            -1,
            Price(data["05. price"]),
            Price(data["06. volume"]),
        )
        return quote

    def get_historic_quote(
        self, ticker: Ticker, start: Time = None, end: Time = None, interval: int = 1
    ):
        """
            Get historic quotes in the time period
        """
        interval = self._adjust_interval(interval)
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval={1}min&apikey={2}".format(
            ticker.symbol, interval, self.key
        )
        data = probe_nyse(url)["Time Series ({0}min)".format(interval)]
        historic_quotes = []
        for time_stamp, values in data.items():
            historic_quotes.append(
                Quote(
                    ticker,
                    datetime.strptime(time_stamp, "%Y-%m-%d %H:%M:%S"),
                    Price(values["1. open"]),
                    Price(values["2. high"]),
                    Price(values["3. low"]),
                    Price(values["4. close"]),
                    -1,
                    Price(values["5. volume"]),
                )
            )
        return historic_quotes

    def get_all_stocks(self):
        """
            Return list of all available stocks
        """
        return self.all_tickers

    def _adjust_interval(self, interval, minimum=1, maximum=60):
        if interval > maximum:
            interval = maximum
        if interval < minimum:
            interval = minimum
        return interval
