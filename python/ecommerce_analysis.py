import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
orders = pd.read_csv("../data/olist_orders_dataset.csv")
order_items = pd.read_csv("../data/olist_order_items_dataset.csv")
customers = pd.read_csv("../data/olist_customers_dataset.csv")
products = pd.read_csv("../data/olist_products_dataset.csv")
payments = pd.read_csv("../data/olist_order_payments_dataset.csv")
category_translation = pd.read_csv("../data/product_category_name_translation.csv")

print("Orders shape:", orders.shape)
print("Order Items shape:", order_items.shape)
print("Customers shape:", customers.shape)
print("Products shape:", products.shape)
print("Payments shape:", payments.shape)
print("Category Translation shape:", category_translation.shape)

# Convert order date to datetime
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

# Extract month
orders['order_month'] = orders['order_purchase_timestamp'].dt.to_period('M')

# Merge orders with order_items
merged_df = pd.merge(orders, order_items, on='order_id')

# Calculate monthly revenue
monthly_revenue = merged_df.groupby('order_month')['price'].sum().reset_index()

# Convert period to string for plotting
monthly_revenue['order_month'] = monthly_revenue['order_month'].astype(str)

# Plot
plt.figure()
plt.plot(monthly_revenue['order_month'], monthly_revenue['price'])
plt.xticks(rotation=45)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../visuals/chart_name.png")
plt.show()


# Merge order_items with products
product_df = pd.merge(order_items, products, on='product_id')

# Merge with category translation
product_df = pd.merge(product_df, category_translation, on='product_category_name')

# Calculate revenue by category
category_revenue = product_df.groupby('product_category_name_english')['price'].sum().reset_index()

# Sort and take top 10
top_categories = category_revenue.sort_values(by='price', ascending=False).head(10)

# Plot
plt.figure()
plt.bar(top_categories['product_category_name_english'], top_categories['price'])
plt.xticks(rotation=45)
plt.title("Top 10 Categories by Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../visuals/chart_name.png")
plt.show()

# Count orders per customer
customer_orders = pd.merge(customers, orders, on='customer_id')
customer_counts = customer_orders.groupby('customer_unique_id')['order_id'].nunique().reset_index()

# Classify customers
customer_counts['customer_type'] = customer_counts['order_id'].apply(
    lambda x: 'One-Time' if x == 1 else 'Repeat'
)

# Count customer types
customer_type_counts = customer_counts['customer_type'].value_counts()

# Plot
plt.figure()
plt.bar(customer_type_counts.index, customer_type_counts.values)
plt.title("Customer Type Distribution")
plt.xlabel("Customer Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("../visuals/chart_name.png")
plt.show()