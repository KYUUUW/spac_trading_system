import pandas as pd

from DBConnection import get_connection
connection = get_connection()

def import_all_company_tickers():
    list = pd.read_csv('../data/spac_list.csv')
    return list['Post-SPAC Ticker Symbol']


if __name__ == '__main__':
    import_all_company_tickers()
