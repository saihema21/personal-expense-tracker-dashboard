# src/expense_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load Data
# -------------------------------
def load_data():
    df = pd.read_csv("data/expenses.csv")
    print("\n✅ Data Loaded Successfully!\n")
    print(df.head())
    return df


# -------------------------------
# 2. Data Cleaning
# -------------------------------
def clean_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'])
    df.dropna(inplace=True)

    print("\n✅ Data Cleaned!\n")
    return df


# -------------------------------
# 3. Category-wise Analysis
# -------------------------------
def category_analysis(df):
    category_spending = df.groupby('category')['amount'].sum()

    print("\n📊 Category-wise Spending:\n")
    print(category_spending)

    return category_spending


# -------------------------------
# 4. Monthly Analysis
# -------------------------------
def monthly_analysis(df):
    df['month'] = df['date'].dt.to_period('M')
    monthly_spending = df.groupby('month')['amount'].sum()

    print("\n📅 Monthly Spending:\n")
    print(monthly_spending)

    return monthly_spending


# -------------------------------
# 5. Payment Method Analysis
# -------------------------------
def payment_analysis(df):
    payment_spending = df.groupby('payment_method')['amount'].sum()

    print("\n💳 Payment Method Spending:\n")
    print(payment_spending)

    return payment_spending


# -------------------------------
# 6. Visualization
# -------------------------------
def create_charts(category_spending, monthly_spending, payment_spending):

    # Category Bar Chart
    category_spending.plot(kind='bar', title='Category-wise Spending')
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("images/category_chart.png")
    plt.show()

    # Monthly Line Chart
    monthly_spending.plot(kind='line', marker='o', title='Monthly Spending')
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("images/monthly_chart.png")
    plt.show()

    # Payment Pie Chart
    payment_spending.plot(kind='pie', autopct='%1.1f%%', title='Payment Methods')
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("images/payment_chart.png")
    plt.show()


# -------------------------------
# 7. Main Function
# -------------------------------
def main():
    df = load_data()
    df = clean_data(df)

    category_spending = category_analysis(df)
    monthly_spending = monthly_analysis(df)
    payment_spending = payment_analysis(df)

    create_charts(category_spending, monthly_spending, payment_spending)


if __name__ == "__main__":
    main()
    filtered_df.to_csv("outputs/filtered_expenses.csv", index=False)