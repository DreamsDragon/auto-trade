"""
    This is to represent human eyes.
    This will return fixed tickers
"""
from autotrade.eyes import BaseEyes
from autotrade.misc import Ticker


class HumanEyes(BaseEyes):
    """
    Object to replicate human eyes
    """

    def __init__(self, tickers: dict) -> None:
        """
            Initalize with tickers we want it to return

        Args:
            tickers (dict): Key is ticker symbol and value is ticker name
        """
        super().__init__()
        self.tickers = []
        for sym, ticker_name in tickers.items():
            self.tickers.append(Ticker(sym, ticker_name))

    def observe(self, *args, **kwargs) -> list[Ticker]:
        """
            Returns the list of tickers to observe

        Args:

        Returns:
            list(Ticker): list of tickers to watch out for
        """
        return self.tickers