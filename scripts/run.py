
if __name__=="__main__":
    from autotrade.brain.ran_brain import RandomBrain
    from autotrade.eyes.human import HumanEyes
    from autotrade.market.historic import HistoricMarket
    from autotrade.traders.simple import SimpleTrader

    from datetime import datetime,timedelta

    start = datetime.today() - timedelta(days=5)
    end = datetime.today()
    interval = "5m"
    tickers = {"AAPL":"Apple Inc"}
    start_cred = 5000
    eyes = [HumanEyes(tickers)]
    markets = [HistoricMarket(start, end, interval)]
    traders = [SimpleTrader(start_cred)]

    brain = RandomBrain(eyes,markets,traders)

    total_counters = 1
    current_counter = 0

    while True:
        brain.act()
        current_counter+=1
        for m in markets:
            m._up_counter()
        if current_counter>=total_counters:
            break