"""
    Module containing different dataclasses used through 
    out the project
"""

from dataclasses import dataclass
from datetime import datetime


Time = datetime


@dataclass
class Ticker:
    symbol: str
    name: str
