import yfinance
import pandas as pd
import json
import pymysql
import sys
from DBConnection import DBConnection

dbc = DBConnection()
connection = dbc.get_connection()

def insert_prices (ticker, ohlc_prices, conn):
    for r in ohlc_prices.itertuples():
        sql = f"REPLACE INTO prices values ('{ticker}', "\
          f"'{r.Index}', '{r.Open}', '{r.High}', "\
          f"'{r.Low}', '{r.Close}', '{r.Volume}')"

        with conn.cursor() as curs:
            curs.execute(sql)


def fetch_price(ticker, start, end):
    stock = yfinance.Ticker(ticker)
    return stock.history(start=start, end=end)


def get_spacs(from_ipo_date, to_ipo_date=None):
    df = pd.read_csv('../data/spac_list.csv')

    df = df[df['SPAC IPO Date'] >= from_ipo_date]
    if(to_ipo_date):
        df = df[df['SPAC IPO Date'] >= to_ipo_date]
    return df


def update_spac_prices(from_ipo_date):
    spacs = get_spacs(from_ipo_date)

    for r in spacs.itertuples():
        print(f"Fetching {r[3]}")

        ohlc_prices = fetch_price(r[2], r[15], r[6])
        insert_prices(r[2], ohlc_prices, connection)

if __name__ == '__main__':
    from_date = sys.argv[1]
    update_spac_prices(from_date)
