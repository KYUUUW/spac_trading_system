import pandas as pd
import sys
from PriceImporter import get_prices
from datetime import datetime
from datetime import date

def get_duration(prices: pd.DataFrame, threshold):
    """get duration from IPO to daily price change more than threshold percent"""

    ipo_date = prices["date"][0]

    prices['changed'] = (prices['close'] - prices['close'].shift(1)) / prices['close'] * 100
    prices['changed'][0] = 0

    for i in range(0, prices.shape[0]):

        if prices['changed'][i] > threshold:
            return (prices['date'][i] - ipo_date).days, prices.iloc[i]

    return 0


if __name__ == '__main__':
    result = get_duration(get_prices('GOEV'), 5)
    print(result)
