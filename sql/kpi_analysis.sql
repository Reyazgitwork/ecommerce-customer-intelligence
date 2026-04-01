-- KPI Analysis

SELECT SUM(price) AS total_revenue FROM order_items;

SELECT COUNT(DISTINCT order_id) AS total_orders FROM orders;

SELECT COUNT(DISTINCT customer_unique_id) AS total_customers FROM customers;

SELECT SUM(price) / COUNT(DISTINCT order_id) AS avg_order_value FROM order_items;