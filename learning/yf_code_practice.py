import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# ✅ Display settings for wide terminal view (optional)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# ✅ Create the 'data' folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# ✅ Fetch last 5 days of Reliance data
reliance = yf.Ticker("RELIANCE.NS")
data = reliance.history(period="5d", interval="1d")

# ✅ Filter only required columns
filtered_data = data[["Open", "High", "Low", "Close", "Volume"]]
print(filtered_data)

# ✅ Save to CSV with today's date
cur_time = datetime.now().strftime("%Y-%m-%d")
filename = f"data/reliance_{cur_time}.csv"
filtered_data.to_csv(filename, index=False)

# ✅ Bonus: Intraday data fetch for another stock
trent = yf.Ticker("TRENT.NS")
trent_data = trent.history(period="1d", interval="5m")
print(trent_data[["Open", "High", "Low", "Close", "Volume"]])
