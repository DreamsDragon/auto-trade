"""
    Traders should be able to buy and sell as we want
"""
from abc import ABC,abstractmethod

from autotrade.misc import Order

class BaseTrader(ABC):
    """
        Abstract trader class
    """
    def __init__(self) -> None:
        super().__init__()
    
    def trade(self,order:Order):
        """
            Finish the given Order
        Args:
            order (Order): Order to finish
        """
        pass