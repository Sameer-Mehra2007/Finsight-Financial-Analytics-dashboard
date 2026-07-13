# FOR CHARTS CREATION 
 
import matplotlib.pyplot as plt
import seaborn as sns

def revenue_expense_chart(df):
    fig, ax = plt.subplots()
    ax.plot(df['Month'], df['Revenue'], label='Revenue', marker='o')
    ax.plot(df['Month'], df['Expenses'], label='Expenses', marker='o')
    
    #ax.set_title("Revenue vs Expenses")
    ax.set_xticks(range(1, len(df) + 1))
    ax.set_xticklabels(df['Month'], rotation=45)
    ax.legend()
    return fig

def profit_bar_chart(df):
    fig, ax = plt.subplots()
    ax.bar(df['Month'], df['Profit'], color='green')
   
    #ax.set_title("Monthly Profits")
    ax.set_xticks(range(1, len(df) + 1))
    ax.set_xticklabels(df['Month'], rotation=45)
   
    return fig

def correlation_heatmap(df):
    fig, ax = plt.subplots()
    corr = df[['Revenue', 'Expenses', 'Profit' ]].corr()
    
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    #ax.set_title("Correlation Heatmap")
    
    return fig

if __name__ == "__main__":
    from data_processor import load_and_clean_data

    df = load_and_clean_data("Book2.csv")

    fig1 = revenue_expense_chart(df)
    fig1.savefig("revenue_expense_chart.png")

    fig2 = profit_bar_chart(df)
    fig2.savefig("profit_bar_chart.png")

    fig3 = correlation_heatmap(df)
    fig3.savefig("correlation_heatmap.png")

    print("All charts saved successfully!")

