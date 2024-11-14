import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# List of stock and ETF ticker symbols (updated)
tickers = [
    "RELIANCE.NS",  # Reliance Industries
    "TCS.NS",       # Tata Consultancy Services
    "HDFCBANK.NS",  # HDFC Bank
    "INFY.NS",      # Infosys
    "BHARTIARTL.NS",  # Bharti Airtel (updated)
    "NIFTYBEES.NS", # Nifty 50 ETF
    "HINDUNILVR.NS", 
    "ITC.NS", 
    "ICICIBANK.NS",
    "KOTAKBANK.NS",
    "LT.NS",
    "BAJFINANCE.NS"
]

# Fetch the data for the last 3 years
data = yf.download(tickers, start="2021-11-01", end="2024-11-01")['Adj Close']

# Save the data to CSV for later use
data.to_csv('indian_assets_data.csv')

# Plotting time series graphs for each asset
data.plot(figsize=(10, 6))
plt.title("Price Data of Selected Indian Assets (Last 3 Years)")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price (INR)")
plt.legend(tickers)
plt.grid(True)
plt.show()

# Plot histograms of returns for each asset
returns = data.pct_change().dropna()  # Daily returns
returns.plot.hist(bins=50, alpha=0.7, figsize=(10, 6))
plt.title("Histogram of Returns for Selected Indian Assets")
plt.xlabel("Daily Returns")
plt.ylabel("Frequency")
plt.legend(tickers)
plt.grid(True)
plt.show()

# Display descriptive statistics for the returns
descriptive_stats = returns.describe()
print(descriptive_stats)
