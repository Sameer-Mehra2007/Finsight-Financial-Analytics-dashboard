import sqlite3
import pandas as pd

def save_to_db(df, db_name="finsight.db"):
    
    conn = sqlite3.connect(db_name)
    df.to_sql("revenue_data", conn, if_exists = "replace", index = False)
    
    conn.close()
    print("Data saved to database!")

def run_query(query, db_name="finsight.db"):
    
    conn = sqlite3.connect(db_name)
    reuslt = pd.read_sql(query, conn)
    conn.close()
    return reuslt

if __name__ =="__main__":
    from data_processor import load_and_clean_data
    
    df = load_and_clean_data("Book2.csv")
    save_to_db(df)

    top_months = run_query("SELECT * FROM revenue_data ORDER BY Revenue DESC LIMIT 3")
    print("Top 3 Months by Revenue: ")
    print(top_months)

    avg_profit = run_query("Select AVG(Profit) as Average_Profit From revenue_data")
    print("Average Profit: ")
    print(avg_profit)
    
    total_expenses = run_query("Select Sum(Expenses) as Total_Expenses From revenue_data")
    print("Total Expenses:")
    print(total_expenses)

