from DBConnection import get_connection
import pandas as pd

connection = get_connection()


def get_prices(ticker):
    sql = f"SELECT * FROM prices WHERE code='{ticker}'"
    prices = pd.read_sql(sql, connection)
    return prices
