"""
    Miscellaneous data types and functions use through out
"""
from dataclasses import dataclass
from datetime import datetime

price_type = float  # Datatype for price
quantity_type = int  # Datatype for quantity
volume_type = float  # Datatype for volume


@dataclass
class Ticker:
    symbol: str  # Ticker symbol
    name: str  # Ticker name

    def __hash__(self) -> int:
        return (str(self.symbol) + str(self.name)).__hash__()


@dataclass
class Order:
    ticker: Ticker  # ticker to buy/sell
    quantity: quantity_type  # How much to buy sell
    unit_price: price_type  # Per unit price
    type: str  # Type of order (buy or sell)

    @property
    def price(self):
        return self.quantity * self.unit_price


@dataclass
class Quote:
    ticker: Ticker  # Ticker for which the quote is genreated
    price: price_type  # price quoted
    volume: volume_type  # volume being traded
    quote_datetime: datetime  # Datetime when the quote was taken
