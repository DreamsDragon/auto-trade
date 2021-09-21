"""
    Base Indicator
"""
from abc import ABC,abstractmethod
from dataclasses import dataclass

@dataclass
class Indication():
    action:int
    
    def __post_init__(self):
        action_types = {1:"buy",2:"sell",3:"hold"}
        action_to_do = action_types.get(self.action,"hold")
        self.action = action_to_do

class BaseIndicator(ABC):
    """
        Base Indicator
    """
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def get_indication(self,*args,**kwargs)->Indication:
        """
            Returns an Indication
        """
        pass