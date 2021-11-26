"""
    The eyes must look at available data and decide what stocks to look out for
"""

from abc import ABC, abstractmethod


class BaseEyes(ABC):
    """
    Abstract Eyes
    """

    def __init__(self) -> None:
        super().__init__()

    def observe(self, *args, **kwargs):
        """
        Observe the markets and return what to buy/sell
        """
        pass