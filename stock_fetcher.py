import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, period="1mo"):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)
        return df

    except Exception as e:
        print(f"Stock fetch error: {e}")   # Helpful for debugging
        return pd.DataFrame()


if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g. TCS.NS): ")
    period = input("Enter period (e.g. 1mo, 3mo, 1y): ")

    df = fetch_stock_data(ticker, period)
    print(df.head())