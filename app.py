import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("sales_data.csv", encoding="latin1")
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Page title
st.title("🚀 SalesSense AI")
st.subheader("Your Smart Business Dashboard")

# ---- FILTERS ----
st.sidebar.header("🔍 Filters")
region = st.sidebar.multiselect("Select Region", options=df["Region"].unique(), default=df["Region"].unique())
category = st.sidebar.multiselect("Select Category", options=df["Category"].unique(), default=df["Category"].unique())

# Apply filters
df_filtered = df[df["Region"].isin(region) & df["Category"].isin(category)]

# ---- KPI CARDS ----
st.write("### 📊 Quick Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${df_filtered['Sales'].sum():,.2f}")
col2.metric("Total Orders", f"{df_filtered['Order ID'].nunique()}")
col3.metric("Total Profit", f"${df_filtered['Profit'].sum():,.2f}")

# ---- CHARTS ----
st.write("### 🛒 Sales by Category")
category_sales = df_filtered.groupby("Category")["Sales"].sum().reset_index()
fig = px.bar(category_sales, x="Category", y="Sales", color="Category", title="Sales by Category")
st.plotly_chart(fig)

st.write("### 🌍 Sales by Region")
region_sales = df_filtered.groupby("Region")["Sales"].sum().reset_index()
fig2 = px.pie(region_sales, values="Sales", names="Region", title="Sales by Region")
st.plotly_chart(fig2)

st.write("### 📈 Monthly Sales Trend")
df_filtered["Month"] = df_filtered["Order Date"].dt.to_period("M").astype(str)
monthly_sales = df_filtered.groupby("Month")["Sales"].sum().reset_index()
fig3 = px.line(monthly_sales, x="Month", y="Sales", title="Monthly Sales Trend")
st.plotly_chart(fig3)