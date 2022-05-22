import requests
import pandas as pd
import json
import numpy as np
import datetime as dt


import yfinance as yf


symbols = {'AAPL':yf.Ticker("AAPL"),
        'GOOG':yf.Ticker("GOOG"),
        'AMZN':yf.Ticker("AMZN"),
     }



def get_df():
    df = pd.DataFrame()
    for stock in symbols.items():
        df2 = pd.DataFrame(stock[1].history(period="1d", interval="1d")).reset_index()
        df2['Symbol'] = stock[0]
        df = df.append(df2, ignore_index=False)

        
    return df

    
# data = get_df()
# print(data.head())
# print(data.info())







