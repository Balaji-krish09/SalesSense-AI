import plotly.express as px
import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("sales_data.csv", encoding="latin1")

# Page title
st.title("🚀 SalesSense AI")
st.subheader("Your Smart Business Dashboard")

# Show raw data
st.write("### 📦 Raw Sales Data")
st.dataframe(df.head(10))

# Basic stats
st.write("### 📊 Quick Stats")
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${df['Sales'].sum():,.2f}")
col2.metric("Total Orders", f"{df['Order ID'].nunique()}")
col3.metric("Total Profit", f"${df['Profit'].sum():,.2f}")

# Sales by Category Chart
st.write("### 🛒 Sales by Category")
category_sales = df.groupby("Category")["Sales"].sum().reset_index()
fig = px.bar(category_sales, x="Category", y="Sales", color="Category", title="Sales by Category")
st.plotly_chart(fig)