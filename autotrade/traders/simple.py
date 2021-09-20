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

    def trade(self, order: Order):
        price = order.price
        if order.type == "sell":
            # Sell stocks
            nb_owned = self.portfolio.get(order.ticker, 0)
            if nb_owned >= 0:
                self._credits += order.unit_price * min(nb_owned, order.quantity)
                self.portfolio[order.ticker] -= nb_owned
                if self.portfolio[order.ticker] == 0:
                    self.portfolio.pop(order.ticker)

        elif order.type == "buy":
            # Buy stocks
            self._credits -= price
            self.portfolio.setdefault(order.ticker, 0)
            self.portfolio[order.ticker] += order.quantity

    def get_credits(self):
        return self._credits

    def get_portfolio(self):
        return self.portfolio