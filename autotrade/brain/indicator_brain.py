"""
    Brain that uses multiple indicators and does the majority action
"""

from autotrade.brain.ran_brain import RandomBrain
from autotrade.misc import Order
from autotrade.brain.indicators import BaseIndicator


class IndicatorBrain(RandomBrain):
    def __init__(
        self,
        eyes,
        markets,
        indicators: list[BaseIndicator],
        traders,
        chunk_size: int = 10,
    ) -> None:
        self.eyes = eyes
        self.markets = markets
        self.traders = traders
        self.chunk_size = chunk_size
        self.indicators = indicators
        super().__init__(eyes, markets, traders, chunk_size)

    def act(self):
        tickers_to_observe = self._get_what_to_observe()
        for ticker in tickers_to_observe:
            credits = self._get_credits()
            portfolio = self._get_portfolio()
            order = Order(ticker, self.chunk_size, 0, "hold")
            indications = {}
            for m in self.markets:
                for i in self.indicators:
                    indication = i.get_indication(ticker, m)
                    indications.setdefault(indication.action, 0)
                    indications[indication.action] += 1
            selected_indication = sorted(indications.items(), key=lambda x: x[1])
            for mv, _ in selected_indication:
                if mv == "buy":
                    quote = self._get_info_about(ticker, "buy")
                    price = quote.price
                    if price * self.chunk_size <= credits:
                        order = Order(ticker, self.chunk_size, price, "buy")
                    break
                elif mv == "sell" and ticker in portfolio:
                    quote = self._get_info_about(ticker, "sell")
                    price = quote.price
                    order = Order(ticker, self.chunk_size, price, "sell")
                    break
            if order is not None:
                self.execute_order(order)
