# 📈 Financial Data Processing and Analysis

A Python-based project that automates the retrieval, processing, and visualization of stock market data. It fetches real-time data from the Alpha Vantage API, computes key financial indicators like Moving Averages and Volatility, exports processed data to Excel, and generates insightful stock trend visualizations.

---

## 🚀 Features

- 📊 Fetch real-time stock data from Alpha Vantage API  
- 📈 Calculate 50-day & 200-day Moving Averages  
- 📉 Compute 20-day rolling Volatility  
- 📁 Export processed data to Excel  
- 🖼️ Visualize stock prices and moving averages with Matplotlib  
- ✅ Clean, modular, and beginner-friendly Python code

---

## 🧠 Tech Stack

- **Language:** Python 3.x  
- **Libraries:**  
  - `requests` – for API data fetching  
  - `pandas` – for data manipulation  
  - `numpy` – for numeric calculations  
  - `matplotlib` – for charting  
  - `openpyxl` – for Excel file handling  

---

## ⚠️ Challenges Faced

API rate limits (5 requests/min for free tier)

Handling JSON structure and converting to clean DataFrame

Ensuring accurate alignment in time-series plots
