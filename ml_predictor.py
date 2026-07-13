import numpy as np
from sklearn.linear_model import LinearRegression

def predict_next_month_revenue(df):
    # Create a simple number for each month (0 1 2 ...)
    df['Month_Number'] = range(1, len(df) + 1)

    X = df[['Month_Number']]   #input : for month : 0 1 2 ...
    y = df['Revenue']          #output : for revenue of the month

    model = LinearRegression()
    model.fit(X, y)

    next_month_number = [[len(df) + 1]]   #the month after the last one
    predicted_revenue = model.predict(next_month_number)

    return predicted_revenue[0]

if __name__ == "__main__":
    from data_processor import load_and_clean_data

    df = load_and_clean_data("Book2.csv")
    prediction = predict_next_month_revenue(df)
    print(f"Predicted Revenue for Next Month : {prediction:.2f}")

#Adding prediction line of stock tracker chart, showing where the price might head over the next 7 days, based on the last days of data. 
def predict_stock_trend(df_stock, days_ahead=7):
    # Create a simple number for each day (0, 1, 2, ...)
    df_stock = df_stock.reset_index()
    df_stock['Day_Number'] = range(1, len(df_stock) + 1)

    X = df_stock[['Day_Number']]  # Input: for day: 0, 1, 2, ...
    y = df_stock['Close']         # Output: for closing price of the day

    model = LinearRegression()
    model.fit(X, y)

    future_days = [[len(df_stock) + i] for i in range(1, days_ahead + 1)] # The days after the last one
    predicted_prices = model.predict(future_days)

    return predicted_prices