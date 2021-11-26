from autotrade.brain.indicators import Indication, BaseIndicator
from autotrade.misc import Ticker, Quote, price_type
from autotrade.market import BaseMarket
from autotrade.brain.indicators.moving_avg import MA

import numpy as np


class BollingerBands(BaseIndicator):
    def __init__(self, nb_smoothing=20, nb_std=2):
        self.nb_smoothing = nb_smoothing
        self.nb_std = nb_std
        self.ma = MA(nb_smoothing)

    def get_indication(
        self, ticker: Ticker, market: BaseIndicator, *args, **kwargs
    ) -> Indication:
        past_quotes = market.get_historic_data(ticker, self.nb_smoothing)
        if len(past_quotes) < self.nb_smoothing:
            return Indication(3)
        ma = self.ma._calculate_mv_avg(past_quotes)
        std = np.std([q.price for q in past_quotes]) * self.nb_std
        bolu = ma + std
        bold = ma - std

        current_price = past_quotes[-1].price
        if current_price > bolu:
            # Sell when price is more than upper band
            return Indication(2)
        if current_price < bold:
            # Buy when price is less than lower band
            return Indication(1)
        if current_price <= bolu and current_price >= bold:
            # valid case
            if current_price > ma:
                # buy
                return Indication(1)
            else:
                # sell
                return Indication(2)
        return Indication(3)
