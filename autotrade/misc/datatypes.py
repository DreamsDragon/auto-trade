"""
    Module containing different dataclasses used through 
    out the project
"""

from dataclasses import dataclass
from datetime import datetime


Time = datetime
Price = float
Quantity = int


@dataclass
class Ticker:
    symbol: str
    name: str


@dataclass
class Quote:
    ticker: Ticker
    time: Time
    open_price: Price
    high: Price
    low: Price
    close: Price
    price: Price
    volume: Quantity

    @property
    def open(self):
        return self.open_price
