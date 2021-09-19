"""
    Market should have information regarding different stocks that we need.
    We can have multiple markets to get information from different sources
"""
from abc import abstractmethod, ABC


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
