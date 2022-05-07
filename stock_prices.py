import requests
import pandas as pd
import json
from google.cloud import bigquery
from google.oauth2 import service_account
from pandas.io import gbq
import pandas_gbq
import numpy as np
import datetime as dt
# import gcsfc

from google_auth_oauthlib import flow

import yfinance as yf


# url = "https://yfapi.net/v8/finance/spark"
# # https://yfapi.net/v8/finance/spark?interval=1mo&range=5y&symbols=AAPL%2CGOOG.AMZN

# def params():
#     return {"interval": "1mo",
#         "range": "5y",
#         "symbols": "AAPL,GOOG,AMZN"
#         }

# def headers():
#     return {
#     'x-api-key': "7O8sgbDKBP9WQC9SrJBjoaME8Q0rDFxM43hWyzTn"
#     }

# def call(url, method = requests.get):
#     result = method(url, headers=headers(), params=params())
#     print(result.url)
#     print(result)
#     result.raise_for_status()
#     return result.json()

# stock_prices = call(url)
# stock_prices = stock_prices
# symbols = "AAPL,GOOG,AMZN"
symbols = {'AAPL':yf.Ticker("AAPL"),
        'GOOG':yf.Ticker("GOOG"),
        'AMZN':yf.Ticker("AMZN"),
     }

 

def params(): 
   return {
    'period':'1d',
    'interval':'1d',
    'group_by':'ticker'
    }



def get_df():
    df = pd.DataFrame()
    # print(df.head())
    for stock in symbols.values():
        df2 = pd.DataFrame(stock.history(params=params)).reset_index()
        df2['Symbol'] = stock
        df = df.append(df2, ignore_index=False)

        
    return df

    
data = get_df()
print(data.head())
print(data.info())







