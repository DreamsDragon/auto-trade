"""
    The Brain of the system. The brain should be able to look at any information it needs 
    and has to make two decisions. 
    1. Buy/Sell/Hold
    2. How much to buy/sell 
"""
from abc import ABC, abstractmethod

from autotrade.misc import price_type, quantity_type


class BaseBrain(ABC):
    """
    Abstract object for brain
    """

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def decide(self, *args, **kwargs) -> tuple(price_type, quantity_type):
        """
        Decide if we buy/sell/hold and how much to buy
        """
        pass