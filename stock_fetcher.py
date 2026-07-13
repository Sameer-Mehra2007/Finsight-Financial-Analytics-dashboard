import yfinance as yf

def fetch_stock_data(ticker, period="1mo"):
    
    stock = yf.Ticker(ticker)
    df = stock.history(period = period)
    return df

if __name__ == "__main__":
    ticker = input("Enter stocks Ticker (e.g TCS.NS) : ")
    period = input("Enter period (e.g 1mo, 3mo, 1y) : ")
    df = fetch_stock_data(ticker, period)
    print(df.head())