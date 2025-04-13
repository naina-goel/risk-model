import yfinance as yf
import pandas as pd

def get_real_market_data(ticker='^GSPC', start='2023-01-01', end='2024-04-01'):
    """
    Downloads historical market price data using yfinance.
    """
    data = yf.download(ticker, start=start, end=end)
    df = data[['Close']].rename(columns={'Close': 'Market_Price'}).reset_index()
    return df

if __name__ == "__main__":
    df = get_real_market_data()
    df.to_csv("real_market_data.csv", index=False)
    print("✅ Market data saved to real_market_data.csv")