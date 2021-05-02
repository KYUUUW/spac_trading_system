from src.DBConnection import get_connection
import pandas as pd

def get_prices(ticker):
    sql = f"SELECT * FROM prices WHERE code='{ticker}'"
    prices = pd.read_sql(sql, get_connection())
    return prices
