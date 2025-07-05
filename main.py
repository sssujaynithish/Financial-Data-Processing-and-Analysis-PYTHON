import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

API_KEY = "ZW3008EJ6G0PH291"
STOCK_SYMBOL = "AAPL"  # Apple Inc.

def fetch_stock_data(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=compact&datatype=json"
    response = requests.get(url)
    data = response.json()
    
    if "Time Series (Daily)" not in data:
        raise ValueError("Invalid API response. Check API Key or symbol.")
    
    stock_data = data["Time Series (Daily)"]
    df = pd.DataFrame.from_dict(stock_data, orient="index")
    df = df.astype(float)  
    
    df.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    }, inplace=True)
    
    df.index = pd.to_datetime(df.index)  
    df = df.sort_index()  
    return df

try:
    stock_df = fetch_stock_data(STOCK_SYMBOL, API_KEY)
except ValueError as e:
    print(e)
    exit()

# Calculate Moving Averages (e.g., 50-day, 200-day)
stock_df["50_MA"] = stock_df["Close"].rolling(window=50).mean()
stock_df["200_MA"] = stock_df["Close"].rolling(window=200).mean()

stock_df["Volatility"] = stock_df["Close"].rolling(window=20).std()

# Save processed data to Excel
stock_df.to_excel("financial_data.xlsx", sheet_name="Stock Data")

plt.figure(figsize=(10, 5))
plt.plot(stock_df.index, stock_df["Close"], label="Closing Price", color="blue")
plt.plot(stock_df.index, stock_df["50_MA"], label="50-day MA", color="green", linestyle="dashed")
plt.plot(stock_df.index, stock_df["200_MA"], label="200-day MA", color="red", linestyle="dashed")
plt.title(f"{STOCK_SYMBOL} Stock Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()
