import pandas as pd
import json

def import_all_company_tickers():
    list = pd.read_csv('../data/spac_list.csv')
    return list['Post-SPAC Ticker Symbol']

def import_available_company():
    with open('../data/available_companies.json', 'r') as f:
        return json.loads(f.read())


if __name__ == '__main__':
    print(import_available_company())
