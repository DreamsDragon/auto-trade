"""
    Simple random selection
"""
from random import shuffle

from autotrade.brain import BaseBrain
from autotrade.misc import Order, Ticker, Quote, price_type, quantity_type


class RandomBrain(BaseBrain):
    """
    Randomly select buy/sell/hold
    """

    def __init__(self, eyes, markets, traders, chunk_size: int = 10) -> None:
        self.eyes = eyes
        self.markets = markets
        self.traders = traders
        self.chunk_size = chunk_size
        super().__init__()

    def act(self):
        tickers_to_observe = self._get_what_to_observe()
        for ticker in tickers_to_observe:
            credits = self._get_credits()
            portfolio = self._get_portfolio()
            quote = self._get_info_about(ticker)
            price = quote.price
            for _ in shuffle([1, 2, 3]):
                if _ == 1 and price * self.chunk_size <= credits:
                    order = Order(ticker, self.chunk_size, price, "buy")
                elif _ == 2 and ticker in portfolio:
                    # Sell
                    order = Order(ticker, self.chunk_size, price, "sell")
                elif _ == 3:
                    # 3 is Hold
                    order = None
                if order is not None:
                    self.execute_order(order)

    def execute_order(self, order: Order):
        for x in self.traders:
            x.trade(order)

    def _get_portfolio(self):
        full_port = {}
        for x in self.traders:
            full_port.update(x.get_portfolio())

    def _get_credits(self):
        return min([x.get_credits() for x in self.traders])

    def _get_what_to_observe(self):
        tickers_to_observe = []
        for eye in self.eyes:
            tickers_to_observe.exted(eye.observe())
        return tickers_to_observe

    def _get_info_about(self, ticker, type: int):
        quote = None
        for market in self.markets:
            new_quote = market.get_info(ticker)
            if quote is None:
                quote = new_quote
            if quote is not None and new_quote is not None:
                if new_quote.price > quote.price and type == 2:
                    # Sell at highest price
                    quote = new_quote
                elif new_quote.price < quote.price and type == 1:
                    # Buy at lowest price
                    quote = new_quote
        return quote