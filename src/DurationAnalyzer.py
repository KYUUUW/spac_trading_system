import pandas as pd
import sys
from PriceImporter import get_prices
from CompanyImporter import import_all_company_tickers
from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt


def get_duration(prices: pd.DataFrame, threshold):
    """get duration from IPO to daily price change more than threshold percent"""

    if prices.shape[0] == 0:
        return 0

    ipo_date = prices["date"][0]

    prices['changed'] = (prices['close'] - prices['close'].shift(1)) / prices['close'] * 100
    prices['changed'][0] = 0

    for i in range(30, prices.shape[0]):

        if prices['changed'][i] > threshold:
            return (prices['date'][i] - ipo_date).days

    return 0


def draw_duration_histogram(_tickers, threshold):
    duration_bucket = []
    count_miss = 0
    for index, ticker in _tickers.items():
        prices = get_prices(ticker)
        duration_days = get_duration(prices, threshold)
        if duration_days != 0:
            duration_bucket.insert(0, duration_days)
        else:
            count_miss += 1

    plt.hist(duration_bucket, bins=50

             )
    plt.show()

    print(f"Missed {count_miss}")


if __name__ == '__main__':
    tickers = import_all_company_tickers()
    draw_duration_histogram(tickers, 15)

