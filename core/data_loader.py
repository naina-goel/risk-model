"""
data_loader.py

This module provides a utility function to fetch real financial market data 
using the Yahoo Finance API via the `yfinance` library. It is used in the 
QuontX-inspired risk modeling pipeline to replace or supplement simulated data 
with actual historical market prices.

The retrieved dataset includes:
- Ticker-based market close prices
- Date-indexed time series
- Cleaned and renamed to match pipeline expectations ('Market_Price')

Use this script independently to download and store real market data for 
further analysis or testing.

Example usage:
    python data_loader.py

This will save the data as: real_market_data.csv
"""

# -------------------------------
# Import Required Libraries
# -------------------------------
import yfinance as yf
import pandas as pd

def get_real_market_data(ticker='^GSPC', start='2023-01-01', end='2024-04-01'):
    """
    Downloads historical market price data using yfinance.
    
    Args:
        ticker (str): Market symbol (default: S&P 500 - ^GSPC)
        start (str): Start date in YYYY-MM-DD
        end (str): End date in YYYY-MM-DD

    Returns:
        DataFrame with columns:
        - Date
        - Market_Price
    """
    data = yf.download(ticker, start=start, end=end)
    df = data[['Close']].rename(columns={'Close': 'Market_Price'}).reset_index()
    return df

if __name__ == "__main__":
    df = get_real_market_data()
    df.to_csv("real_market_data.csv", index=False)
    print("✅ Market data saved to real_market_data.csv")
