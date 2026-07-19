# 📊 FinSight - Financial Analytics Dashboard

FinSight is a full-stack finance analytics web app built entirely in Python. Upload your revenue CSV to instantly see KPI cards, trend charts, SQL-powered insights, and ML-based revenue forecasts. It also includes a live Stock Tracker with real-time price data and a 7-day prediction trend.

🔗 **Live App:** [finsight-finance.streamlit.app](https://finsight-finance.streamlit.app/)

## Features

- 📈 Upload any revenue CSV and get instant KPI cards (Total Revenue, Profit, Margin)
- 📊 Revenue vs Expenses trend chart and monthly profit chart
- 🔮 ML-powered revenue forecast (Linear Regression) for next month
- 📋 SQL-powered insights panel (top months, average profit, total expenses)
- 📥 Export cleaned data as CSV
- 💹 Live Stock Tracker — search any ticker, view candlestick charts
- 🔮 7-day stock price forecast using Linear Regression
- 🎨 Custom-themed, responsive Streamlit UI

## Tech Stack

| Category | Tools |
|---|---|
| Frontend | Streamlit |
| Backend | Python, Pandas, SQLite |
| Visualization | Matplotlib, Seaborn, Plotly |
| Machine Learning | Scikit-learn (Linear Regression) |
| Data Source | User CSV upload + Yahoo Finance API (yfinance) |
| Deployment | Streamlit Cloud |

## Project Structure
finsight/
|--app.py       #Main Streamlit Frontend
|--data_processor.py    #Data cleaning and KPI Calculations
|--data_manager.py      #SQlite database manager
|--stock_fetcher.py     #live stock data via yfinance
|--ml_predictor.py      #Revenue and stock forecasting
|--charts.py            #Chart generation functions
|--requirements.py      #python dependencies
|--.streamlit/config.toml   #Customer theme
|-- Book2.CSV               #Sample dataset