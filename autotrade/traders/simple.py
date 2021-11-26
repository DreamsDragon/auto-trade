"""
    Very simple trader that will always successfully do the trade
"""

from autotrade.traders import BaseTrader
from autotrade.misc import Ticker, Quote, Order, price_type


class SimpleTrader(BaseTrader):
    """
    Simple traders
    """

    def __init__(self, start_credit: int) -> None:
        super().__init__()
        self._credits = start_credit
        self.portfolio = {}
        self.orders = {}

    def trade(self, order: Order):
        price = order.price
        self.orders.setdefault(order.ticker,[])
        if order.type == "sell":
            # Sell stocks
            nb_owned = self.portfolio.get(order.ticker, 0)
            if nb_owned >= 0:
                nb_sold =  min(nb_owned, order.quantity)
                self._credits += order.unit_price *nb_sold
                self.portfolio[order.ticker] -= nb_sold
                if self.portfolio[order.ticker] == 0:
                    self.portfolio.pop(order.ticker)
            self.orders[order.ticker].append(order)

        elif order.type == "buy":
            # Buy stocks
            self._credits -= price
            self.portfolio.setdefault(order.ticker, 0)
            self.portfolio[order.ticker] += order.quantity
            self.orders[order.ticker].append(order)
            

    def get_credits(self):
        return self._credits

    def get_portfolio(self):
        return self.portfolio
    
