"""
    Miscellaneous data types and functions use through out
"""
from dataclasses import dataclass

price_type = float  # Datatype for price
quantity_type = int  # Datatype for quantity


@dataclass
class Ticker:
    symbol: str  # Ticker symbol
    name: str  # Ticker name


@dataclass
class Order:
    ticker: Ticker  # ticker to buy/sell
    quantity: quantity_type  # How much to buy sell
    type: str  # Type of order (buy or sell)
