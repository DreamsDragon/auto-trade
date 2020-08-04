"""
    Module containing different dataclasses used through 
    out the project
"""

from dataclasses import dataclass
from datetime import datetime


Time = datetime


@dataclass
class Ticker:
    ticker_symbol: str
    name: str
