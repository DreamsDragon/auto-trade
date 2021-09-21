"""
    Market should have information regarding different stocks that we need.
    We can have multiple markets to get information from different sources
"""
from abc import abstractmethod, ABC
from autotrade.misc import Ticker, Quote

class BaseMarket(ABC):
    """
    Abstract market object
    """

    def __init__(self) -> None:
        super().__init__()

    def get_info(self, *args, **kwargs):
        """
        Get required information from this Market
        """
        pass

    def get_historic_data(self, ticker: Ticker, nb_past_quotes: int) -> list[Quote]:
        """
            Get the historic data for the ticker
        Args:
            ticker (Ticker): Ticker to get the data for
            nb_past_quotes (int): Number of past ticks to return

        Returns:
            list[Quote]: list of historic quotes
        """