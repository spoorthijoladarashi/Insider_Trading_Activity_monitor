import pandas as pd

def load_data():

    holdings = pd.read_csv(
        "data/MASTER_DATA_ENRICHED.csv"
    )

    signals = pd.read_csv(
        "data/PREMIUM_CROSS_MARKET_SIGNALS.csv"
    )

    return holdings, signals
