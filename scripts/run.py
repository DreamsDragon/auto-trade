if __name__ == "__main__":
    from autotrade.brain.ran_brain import RandomBrain
    from autotrade.brain.indicator_brain import IndicatorBrain
    from autotrade.brain.indicators.moving_avg import MACD, GoldenCross
    from autotrade.eyes.human import HumanEyes
    from autotrade.market.historic import HistoricMarket
    from autotrade.traders.simple import SimpleTrader
    from autotrade.brain.indicators.bollinger_bands import BollingerBands
    from datetime import datetime, timedelta

    start = datetime.today() - timedelta(days=60)
    end = datetime.today()
    interval = "1h"
    tickers = {"NVDA": "Nvidia"}
    start_cred = 20000
    eyes = [HumanEyes(tickers)]
    markets = [HistoricMarket(start, end, interval)]
    traders = [SimpleTrader(start_cred)]

    # brain = RandomBrain(eyes, markets, traders)
    brain = IndicatorBrain(eyes, markets, [MACD()], traders)
    total_counters = 100
    current_counter = 0

    while True:
        print(current_counter + 1)
        brain.act()
        current_counter += 1
        for m in markets:
            m._up_counter()
        if current_counter >= total_counters:
            break
