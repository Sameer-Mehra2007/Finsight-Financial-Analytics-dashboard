import pandas as pd 

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
#remove rows with missing value
    df = df.dropna()

    df['Month'] = pd.to_datetime(df['Month'], format='%b-%y')
    df['Month'] = df['Month'].dt.strftime('%b-%y')

    df['Profit'] = df['Revenue']-df['Expenses']

    return df

if __name__=="__main__":
    df = load_and_clean_data("Book2.csv")
    print(df.head())

#part-3

def calculate_kpis(df):

    total_revenue = df['Revenue'].sum()
    
    total_profit = df['Profit'].sum()
    
    profit_margin = (total_profit / total_revenue) * 100
    
    #Month-Over_month growth%
    df['MoM_growth'] = df['Revenue'].pct_change() * 100

    print(f"Total Revenue: {total_revenue}")
    
    print(f"Total Profit: {total_profit}")

    print(f"Profit_Margin: {profit_margin:.2f}%")
    print(df[['Month','Revenue','MoM_growth']])

    return total_revenue, total_profit, profit_margin

if __name__=="__main__":
    df = load_and_clean_data("Book2.csv")
    calculate_kpis(df)

#cd Finsight #pyhton data_processor.py

#part-4 (SQL Data_manager.py)    

