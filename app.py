import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from data_manager import save_to_db, run_query
from data_processor import load_and_clean_data, calculate_kpis
from charts import revenue_expense_chart, profit_bar_chart #, correlation_heatmap
from ml_predictor import predict_next_month_revenue,predict_stock_trend
from stock_fetcher import fetch_stock_data
st.set_page_config(
    page_title="Finsight", page_icon=":bar_chart:", layout="wide"
)

#st.title("Finsight :- Financial Analytics Dashboard")
st.markdown("""
    <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            body {
                font-family: 'Roboto', sans-serif;
                background-color: #f5f5f5;
                color: #333;
            }
    </style>
""", unsafe_allow_html=True)        
st.markdown("""
    <div style="text-align: center; background: linear-gradient(90deg, #FF671F, #D4AF37); padding: 25px; border-radius: 12px; margin-bottom: 10px; ">
        <h1 style="color: white; font-family: 'Roboto', sans-serif; font-size: 46px; font-weight: 800; letter-spacing: 1px;margin : 0;">📊Finsight : Financial Analytics Dashboard</h1>
        <p style="color: #E3F2FD; text-align: center;font-size: 18px; margin-top: 10px;">Track your revenue, profits and stock trends performance all in one place.</p>
    </div>
""", unsafe_allow_html=True)
st.caption("Welcome to Finsight - Track your revenue, profits and stock trends performance all in one place.")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Revenue Dashboard", "Stock Tracker"])
st.sidebar.markdown("---")
st.sidebar.markdown("Built with using Streamlit | Finsight © 2026.")
if page == "Revenue Dashboard":
    st.header("Revenue Dashboard")

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        with st.spinner("Processing data..."):
            
            df = load_and_clean_data(uploaded_file)
            st.success("CSV uploaded successfully ")
            total_revenue, total_profit, profit_margin = calculate_kpis(df)
        with st.container(border=True):
            col1, col2, col3 = st.columns(3)
            st.write(f"You selected: {page}")
            col1.metric("Total Revenue", f"₹{total_revenue:,.2f}")
            col2.metric("Total Profit", f"₹{total_profit:,.2f}")
            col3.metric("Profit Margin", f"{profit_margin:.2f}%")

            st.subheader("📈Revenue vs Expenses ")
            fig1 = revenue_expense_chart(df)
            st.pyplot(fig1)
            st.divider()
            
            st.subheader("💰Monthly Profits")
            fig2 = profit_bar_chart(df)
            st.pyplot(fig2)
            st.divider()
            #st.subheader("Correlation Heatmap")
            #fig3 = correlation_heatmap(df)
            #st.plotly_chart(fig3)

            st.subheader("🔮Next Month Revenue Prediction")
            prediction = predict_next_month_revenue(df)
            st.metric("Predicted Revenue for Next Month: ", f"₹{prediction:,.2f}")
            st.divider()

##SQL Insights START
            st.subheader("📊SQL Insights")
            save_to_db(df)
            top_months = run_query("Select * FROM revenue_data  order by Revenue desc limit 3")
            st.write("**Top 3 Months by Revenue:**")
            #st.dataframe(top_months)
            styled_df = top_months.style.set_properties(**{'background-color': "#E3F2FD"})
            st.dataframe(styled_df)
            
            avg_profit = run_query("Select AVG(Profit) as avg_profit FROM revenue_data")
            st.write("**Average Profit:**")
            styled_df = avg_profit.style.set_properties(**{'background-color': "#E3F2FD"})
            st.dataframe(styled_df)
            #st.dataframe(avg_profit)

            total_expenses = run_query("Select SUM(Expenses) as total_expenses from revenue_data")
            st.write("**Total Expenses:**")
            styled_df = total_expenses.style.set_properties(**{'background-color': "#E3F2FD"})
            st.dataframe(styled_df)

            st.success("Data processed successfully!")

            st.download_button(
                label="Download Cleaned Data as CSV",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name="cleaned_data.csv",
                mime="text/csv",
            )
#stock tracker page
elif page == "Stock Tracker":
        #st.header("Stock Tracker")
        st.markdown("""
            <div style="text-align: center; background: linear-gradient(90deg, #1E88E5, #0D47A1); padding: 18px; border-radius: 10px; margin-bottom: 15px; ">
                <h2 style="color: white; font-family: 'Roboto', sans-serif; font-size: 46px; font-weight: 800; letter-spacing: 1px;margin : 0;">📈Stock Tracker</h2>
                    
            </div>
        """, unsafe_allow_html=True)
        with st.container(border=True):    
            ticker = st.text_input("Enter Stock Symbol (e.g., AAPL, MSFT):")
            period = st.selectbox("Select Time Period", ["1mo", "3mo", "6mo", "1y"])
            st.divider()
        if ticker:
            with st.spinner("Fetching stock data..."):
                
                df_stock = fetch_stock_data(ticker, period)

                if df_stock.empty:
                   st.warning("Failed to fetch stock data. Please check the symbol and try again.\n\n"
                              "Try symbol like TCS.NS, INFY.NS, AAPL, MSFT etc. Please check your internet connection.")
                else:
                    st.success(f"Stock data fetched successfully of {ticker}")
                    st.divider()
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Open Price", f"₹{df_stock['Open'].iloc[-1]:,.2f}")
                    col2.metric("Close Price", f"₹{df_stock['Close'].iloc[-1]:,.2f}")
                    col3.metric("52 Week High Price", f"₹{df_stock['High'].max():,.2f}")
                    col4.metric("52 Week Low Price", f"₹{df_stock['Low'].min():,.2f}")
                    
                    #st.line_chart(df_stock[['Open', 'Close']])
                    fig_stock = go.Figure(data=[go.Candlestick(x=df_stock.index,
                        open= df_stock['Open'],
                        high= df_stock['High'],
                        low= df_stock['Low'],
                        close= df_stock['Close'],
                        increasing_line_color='#1E885D',
                        decreasing_line_color='#EF5350', name='Candlestick')])
                    
                    #fig_stock.add_trace(go.Scatter(x=df_stock.index, y=df_stock['Open'], mode='lines', name='Open Price', line=dict(color='#1E885D', width= 2)))
                    #fig_stock.add_trace(go.Scatter(x=df_stock.index, y=df_stock['Close'], mode='lines', name='Close Price', line=dict(color='#EF5350', width= 2)))
                    fig_stock.update_layout(title=f"{ticker} Stock Prices ", xaxis_title="Date", yaxis_title="Price (INR ₹)", hovermode='x unified', template="plotly_white",
                    xaxis_rangeslider_visible=False)
                    
                    st.plotly_chart(fig_stock, use_container_width=True)
                
                    st.divider()
                    
                    st.subheader("Next Week Stock Price Prediction")
                    predicted_prices = predict_stock_trend(df_stock)
                    predicted_prices_df = pd.DataFrame({
                        "Day": [f"Day {i+1}" for i in range(len(predicted_prices))],
                        "Predicted Close Price": predicted_prices})
                    st.dataframe(predicted_prices_df)
                    
                    st.divider()
                    st.subheader("Raw Stock Data")
                    st.dataframe(df_stock)
        else:
            st.info("Failed to fetch stock data. Enter a stock ticker above to see data.")        
