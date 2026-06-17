import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Data options
regions = ["North", "South", "East", "West", "Central"]
states = {
    "North": ["Delhi", "Punjab", "Haryana", "UP", "Rajasthan"],
    "South": ["Tamil Nadu", "Karnataka", "Telangana", "Kerala", "Andhra Pradesh"],
    "East": ["West Bengal", "Odisha", "Jharkhand", "Bihar"],
    "West": ["Maharashtra", "Gujarat", "Goa"],
    "Central": ["MP", "Chhattisgarh"]
}
products = {
    "Flat Steel": ["Hot Rolled Coils", "Cold Rolled Coils", "Galvanized Sheets", "Color Coated Sheets"],
    "Long Steel": ["TMT Bars", "Wire Rods", "Structural Steel", "Rails"],
    "Special Steel": ["Stainless Steel", "Alloy Steel", "Tool Steel"]
}
customers = [
    "Larsen & Toubro", "Tata Projects", "Shapoorji Pallonji",
    "Afcons Infrastructure", "NCC Limited", "KEC International",
    "Ashoka Buildcon", "Dilip Buildcon", "PNC Infratech", "IRB Infrastructure"
]
salespersons = ["Rahul Sharma", "Priya Patel", "Amit Singh", "Sneha Reddy", "Vikram Nair"]

# Generate 2000 rows
rows = []
start_date = datetime(2022, 1, 1)

for i in range(2000):
    region = random.choice(regions)
    state = random.choice(states[region])
    category = random.choice(list(products.keys()))
    product = random.choice(products[category])
    quantity = random.randint(10, 500)  # in tonnes
    price_per_tonne = random.randint(45000, 85000)  # in INR
    sales = quantity * price_per_tonne
    profit_margin = random.uniform(0.05, 0.20)
    profit = sales * profit_margin
    order_date = start_date + timedelta(days=random.randint(0, 730))
    ship_date = order_date + timedelta(days=random.randint(3, 15))

    rows.append({
        "Order ID": f"JSW-{2022 + i // 1000}-{str(i+1).zfill(4)}",
        "Order Date": order_date.strftime("%d-%m-%Y"),
        "Ship Date": ship_date.strftime("%d-%m-%Y"),
        "Customer Name": random.choice(customers),
        "Salesperson": random.choice(salespersons),
        "Region": region,
        "State": state,
        "Category": category,
        "Product": product,
        "Quantity (Tonnes)": quantity,
        "Price per Tonne (INR)": price_per_tonne,
        "Sales (INR)": sales,
        "Profit (INR)": round(profit, 2)
    })

df = pd.DataFrame(rows)
df.to_csv("sales_data.csv", index=False)
print("✅ JSW Steel style data generated successfully!")
print(f"Total rows: {len(df)}")
print(df.head())