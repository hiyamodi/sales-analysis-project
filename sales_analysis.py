import pandas as pd

# 1. Load the dataset
df = pd.read_csv('sales_data.csv')

# 2. Handle missing values
# Although initial inspection showed no nulls, we check again 
# and ensure we have data integrity for critical columns
df = df.dropna(subset=['Product']) 
df['Total_Sales'] = df['Total_Sales'].fillna(0)

# 3. Calculate 3 Key Metrics
# Metric 1: Total Sales Revenue
total_revenue = df['Total_Sales'].sum()

# Metric 2: Best-selling Product (by Quantity)
# Group products and find the name and total count for the top one
product_qty = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
best_selling_product_name = product_qty.index[0]
best_selling_product_units = product_qty.iloc[0]

# Metric 3: Average Transaction Value
# Provides insight into the average revenue per sale
average_sale = df['Total_Sales'].mean()

# Additional Metrics for the report
# Revenue by region and product summary
regional_sales = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
product_summary = df.groupby('Product').agg({
    'Quantity': 'sum',
    'Total_Sales': 'sum'
}).sort_values(by='Total_Sales', ascending=False)

# Export the summarized product data to a CSV for stakeholders
product_summary.to_csv('product_sales_summary.csv')

# 4. Generate the formatted report
report = f"""
--- SALES ANALYSIS REPORT ---

1. Total Revenue:         ${total_revenue:,.2f}
2. Average Sale Value:     ${average_sale:,.2f}
3. Best-Selling Product:   {best_selling_product_name} ({best_selling_product_units} units sold)

--- Regional Performance ---
{regional_sales.to_string()}

--- Products by Revenue ---
{product_summary.to_string()}

-----------------------------
"""

print(report)