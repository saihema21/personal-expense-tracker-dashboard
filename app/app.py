import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Expense Tracker", layout="wide")

st.title("💰 Personal Expense Tracker Dashboard")

file = st.file_uploader("Upload your expense CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df['date'])

    # 🔹 Sidebar Filters
    st.sidebar.header("🔍 Filters")

    min_date = df['date'].min()
    max_date = df['date'].max()

    date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date])

    categories = df['category'].unique()
    selected_category = st.sidebar.multiselect("Select Category", categories, default=categories)

    # 🔹 Apply Filters
    filtered_df = df[
        (df['date'] >= pd.to_datetime(date_range[0])) &
        (df['date'] <= pd.to_datetime(date_range[1])) &
        (df['category'].isin(selected_category))
    ]

    # 🔹 Layout
    col1, col2 = st.columns(2)

    # 💰 Total Expense
    total = filtered_df['amount'].sum()
    col1.metric("Total Expense", f"₹ {total}")

    # 📅 Monthly Expense
    filtered_df['month'] = filtered_df['date'].dt.to_period('M')
    monthly = filtered_df.groupby('month')['amount'].sum()
    col2.metric("This Month Expense", f"₹ {monthly.iloc[-1] if not monthly.empty else 0}")

    st.divider()

    # 📊 Category-wise Bar Chart
    st.subheader("📊 Category-wise Expense")
    category_data = filtered_df.groupby('category')['amount'].sum()

    fig1, ax1 = plt.subplots()
    category_data.plot(kind='bar', ax=ax1)
    st.pyplot(fig1)

    # 🥧 Pie Chart
    st.subheader("🥧 Expense Distribution")
    fig2, ax2 = plt.subplots()
    category_data.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
    ax2.set_ylabel("")
    st.pyplot(fig2)

    # 📈 Daily Trend
    st.subheader("📈 Daily Spending Trend")
    daily = filtered_df.groupby('date')['amount'].sum()

    fig3, ax3 = plt.subplots()
    daily.plot(ax=ax3)
    st.pyplot(fig3)

    # 📄 Show filtered data
    st.subheader("📄 Filtered Data")
    st.dataframe(filtered_df)

else:
    st.info("Please upload a CSV file to continue.")