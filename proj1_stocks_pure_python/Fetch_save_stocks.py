import yfinance as yf
import pandas as pd
import os
from datetime import datetime


pd.set_option('display.max_rows', None)      # Display all rows
pd.set_option('display.max_columns', None)

def fetch_data(stock: str):
    share = yf.Ticker(stock)
    data = share.history(period = '5d', interval = '4h')
    filtered = data[["Open", "Close", "High", "Low", "Volume"]]
    print(filtered)
    publish_csv(filtered, stock)


def publish_csv(data, stock_name):

    file = f"{stock_name}_5d_data.csv"
    if os.path.exists("csv_files"):
        # overwrite if exists
        data.to_csv(f"csv_files/{file}", index = False)

    else:
        os.makedirs("csv_files")
        data.to_csv(f"csv_files/{file}", index=False)

fetch_data("RELIANCE.NS")