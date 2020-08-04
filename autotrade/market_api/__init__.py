"""
    Module containing the abstrast market api
"""
from abc import ABC, abstractmethod

from ..misc.datatypes import Ticker, Time


class AbstractMarketAPI(ABC):
    """
        Abstract Maret API
    """

    @abstractmethod
    def get_quote(self, ticker: Ticker):
        """
            Get the live quote of a ticker
        """
        pass

    @abstractmethod
    def get_historic_quote(self, ticker: Ticker, start: Time, end: Time):
        """
            Get historic quotes in the time period
        """
        pass

    @abstractmethod
    def get_all_stocks(self):
        """
            Return list of all available stocks
        """
        pass
