"""
    Contains various moving average indicators
"""
from autotrade.brain.indicators import Indication,BaseIndicator
from autotrade.misc import Ticker,Quote,price_type
from autotrade.market import BaseMarket

def exp_mv_average(values,smoothing=2):
    ema = 0
    for (i,q) in enumerate(values):
        days = i+1
        factor = smoothing/(1+days)
        ema = (q.price *factor) + ema* (1-factor)
    return ema

class EMA(BaseIndicator):

    def __init__(self,nb_ticks:int) -> None:
        """
            Init function for Exponential Moving Averages
        Args:
            nb_ticks (int): Period to calculate the ema for
        """
        self.nb_ticks = nb_ticks
        super().__init__()
    
    def get_indication(self, *args, **kwargs) -> Indication:
        return None
    
    def _calculate_mv_avg(self,quotes:list[Quote],smoothing:int = 2)->price_type:
        """
            Calculate the moving average of the given period
        Args:
            quotes (list[Quote]): [description]

        Returns:
            price_type: EMA value
        """
        sorted_quotes = sorted(quotes,key=lambda x:x.quote_datetime,reverse=True)[:self.nb_ticks][::-1]
        values = [q.price for q in sorted_quotes]
        ema = exp_mv_average(values,smoothing)
        return ema

class MACD(BaseIndicator):

    def __init__(self,signal_size = 9) -> None:
        self.ema_12 = EMA(12)
        self.ema_24 = EMA(24)
        self.signal_size = signal_size
        self.past_macd = []
        super().__init__()
    
    def _add_to_memory(self,macd:price_type):
        self.past_macd.append(macd)
        if len(self.past_macd)>self.signal_size:
            self.past_macd.pop(0)

        
    def get_indication(self,ticker:Ticker,market:BaseMarket, *args, **kwargs) -> Indication:
        indication = 3 # Hold
        macd = self._get_macd(ticker,market)
        if macd is not None:
            self._add_to_memory(macd)
            signal = self._get_signal()
            if signal is not None:
                if macd>signal:
                    indication = 1 # Buy
                elif macd<signal:
                    indication = 2 # Sell
        return Indication(indication)
            
    def _get_signal(self):
        signal_value = None
        if len(self.past_macd)>=self.signal_size:
            signal_value = exp_mv_average(self.past_macd)
        return signal_value
        
    def _get_macd(self,ticker:Ticker,market:BaseMarket)->price_type:
        past_24_quotes = market.get_historic_data(ticker,24)
        if len(past_24_quotes)<24:
            return None
        long_ema = self.ema_24._calculate_mv_avg(past_24_quotes)
        short_ema = self.ema_12._calculate_mv_avg(past_24_quotes)
        return short_ema-long_ema
    
