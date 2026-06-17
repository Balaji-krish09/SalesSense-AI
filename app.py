import streamlit as st
import pandas as pd
import plotly.express as px
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load data
df = pd.read_csv("sales_data.csv", encoding="latin1")
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

# Page title
st.title("🏭 SalesSense AI — JSW Steel Dashboard")
st.subheader("Smart Sales Intelligence for Steel Industry")

# ---- FILTERS ----
st.sidebar.header("🔍 Filters")
region = st.sidebar.multiselect("Select Region", options=df["Region"].unique(), default=df["Region"].unique())
category = st.sidebar.multiselect("Select Category", options=df["Category"].unique(), default=df["Category"].unique())

# Apply filters
df_filtered = df[df["Region"].isin(region) & df["Category"].isin(category)]

# ---- KPI CARDS ----
st.write("### 📊 Quick Stats")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"₹{df_filtered['Sales (INR)'].sum()/10000000:,.2f} Cr")
col2.metric("Total Profit", f"₹{df_filtered['Profit (INR)'].sum()/10000000:,.2f} Cr")
col3.metric("Total Orders", f"{df_filtered['Order ID'].nunique()}")
col4.metric("Total Volume", f"{df_filtered['Quantity (Tonnes)'].sum():,.0f} T")

# ---- CHARTS ----
st.write("### 🏗️ Sales by Product Category")
category_sales = df_filtered.groupby("Category")["Sales (INR)"].sum().reset_index()
fig = px.bar(category_sales, x="Category", y="Sales (INR)", color="Category", title="Sales by Category (INR)")
st.plotly_chart(fig)

st.write("### 🌍 Sales by Region")
region_sales = df_filtered.groupby("Region")["Sales (INR)"].sum().reset_index()
fig2 = px.pie(region_sales, values="Sales (INR)", names="Region", title="Sales by Region")
st.plotly_chart(fig2)

st.write("### 📈 Monthly Sales Trend")
df_filtered["Month"] = df_filtered["Order Date"].dt.to_period("M").astype(str)
monthly_sales = df_filtered.groupby("Month")["Sales (INR)"].sum().reset_index()
fig3 = px.line(monthly_sales, x="Month", y="Sales (INR)", title="Monthly Sales Trend")
st.plotly_chart(fig3)

st.write("### 🏆 Top Products by Sales")
product_sales = df_filtered.groupby("Product")["Sales (INR)"].sum().reset_index().sort_values("Sales (INR)", ascending=False).head(10)
fig4 = px.bar(product_sales, x="Sales (INR)", y="Product", orientation="h", title="Top 10 Products by Sales")
st.plotly_chart(fig4)

# ---- AI INSIGHTS ----
st.write("### 🤖 AI Insights")
if st.button("Generate AI Insights"):
    with st.spinner("AI is analyzing your steel sales data..."):

        top_product = product_sales.iloc[0]["Product"]
        top_region = region_sales.sort_values("Sales (INR)", ascending=False).iloc[0]["Region"]

        summary = f"""
        JSW Steel Sales Dashboard Summary:
        - Total Sales: ₹{df_filtered['Sales (INR)'].sum()/10000000:,.2f} Crores
        - Total Profit: ₹{df_filtered['Profit (INR)'].sum()/10000000:,.2f} Crores
        - Total Orders: {df_filtered['Order ID'].nunique()}
        - Total Volume: {df_filtered['Quantity (Tonnes)'].sum():,.0f} Tonnes
        - Top Category: {category_sales.sort_values('Sales (INR)', ascending=False).iloc[0]['Category']}
        - Top Product: {top_product}
        - Top Region: {top_region}
        - Date Range: {df_filtered['Order Date'].min().date()} to {df_filtered['Order Date'].max().date()}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a senior business analyst for an Indian steel company. Analyze the sales data and give 3 clear actionable business insights in simple English. Use Indian business context."},
                {"role": "user", "content": summary}
            ]
        )

        insight = response.choices[0].message.content
        st.success(insight)