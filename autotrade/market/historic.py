"""
    A historic market uses historic trade data to simulate a real market
"""
from datetime import date, datetime, timedelta

import yfinance as yf

from autotrade.market import BaseMarket
from autotrade.misc import Ticker, Quote, price_type, volume_type


class HistoricMarket(BaseMarket):
    """
    Historic Market object
    """

    def __init__(self, start: datetime, end: datetime, interval: str = "5m") -> None:
        """
            Initialize the historic market object
        Args:
            start (datetime): Time to start the market at
            end (datetime): Time to end the market at. Note that price after this time is same as end time
            interval (str, optional): The interval between ticks. Defaults to "5m".
        """
        super().__init__()
        self.start = start
        self.end = end
        self.interval = interval
        self.__post_init__()
        self.trade_data = {}
        self.counter = 0

    def _up_counter(self):
        """
        Increase the ticker
        """
        self.counter += 1

    def __post_init__(self):
        """
        Do some post initialization stuff
        """
        if self.interval in ["5m", "15m"]:
            time_diff = self.end - self.start
            if time_diff.days >= 6:
                self.end = self.start + timedelta(days=6)

    def _get_data(self, ticker: Ticker):
        """
            Get the required historic data
        Args:
            ticker (Ticker): Ticker to get the data for

        """
        try:
            yticker = yf.Ticker(ticker.symbol)
            hist_data = yticker.history(
                start=self.start.strftime("%Y-%m-%d"),
                end=self.end.strftime("%Y-%m-%d"),
                interval=self.interval,
            )
            return hist_data
        except:
            return None

    def get_info(self, ticker: Ticker) -> Quote:
        """
            Get the current quote

        Args:
            ticker (Ticker): Ticker to get the data for

        Returns:
            Quote: Quote with the required data
        """
        self.trade_data.setdefault(ticker, self._get_data(ticker))
        if self.trade_data[ticker] is not None:
            df = self.trade_data.get(ticker)
            needed_index = max(0, min(self.counter, df.shape[0]))
            row = df.iloc[[needed_index]]
            quote_datetime = row.index.to_pydatetime()[0]
            price = price_type(row["Close"])
            volume = volume_type(row["Volume"])
            return Quote(ticker, price, volume, quote_datetime)
        return None

    def get_historic_data(self, ticker: Ticker, nb_past_quotes: int) -> list[Quote]:
        """
            Get the historic data for the ticker
        Args:
            ticker (Ticker): Ticker to get the data for
            nb_past_quotes (int): Number of past ticks to return

        Returns:
            list[Quote]: list of historic quotes
        """
        old_counter = int(self.counter)
        data_to_return = []
        for _ in range(nb_past_quotes):
            data_to_return.append(self.get_info(ticker))
            self.counter -= 1
        self.counter = old_counter
        return data_to_return[::-1]


if __name__ == "__main__":

    start = datetime.today() - timedelta(days=5)
    end = datetime.today()
    interval = "5m"
    market = HistoricMarket(start, end, interval)

    ticker = Ticker("AAPL", "Apple Inc")
    market.counter = 5
    for x in market.get_historic_data(ticker, 5):
        print(x)
    print()
    print(market.get_info(ticker))