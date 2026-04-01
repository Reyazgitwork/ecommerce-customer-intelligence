# E-commerce Customer Intelligence & Revenue Optimization

## Project Overview
This project analyzes an e-commerce dataset to understand business performance, customer behavior, and product category trends. The goal is to generate actionable business insights using SQL and Python.

## Business Problem
An e-commerce company wants to understand:
- how revenue is performing over time
- which product categories drive the most revenue
- whether customers are returning or buying only once
- where the biggest opportunities for business growth exist

## Tools Used
- **SQL (MySQL)** for data import and business analysis
- **Python (Pandas, Matplotlib)** for data analysis and visualization
- **GitHub** for project presentation

## Dataset
Dataset used: **Olist Brazilian E-commerce Dataset**

Main tables used:
- customers
- orders
- order_items
- products
- payments
- category_translation

## Project Workflow
1. Created project structure
2. Imported CSV files into MySQL
3. Validated and explored the data
4. Calculated business KPIs using SQL
5. Analyzed customer purchase behavior
6. Identified top-performing product categories
7. Built charts in Python

## Key KPIs
- **Total Revenue:** 13,591,643.70
- **Total Orders:** 99,441
- **Total Customers:** 96,096
- **Average Order Value (AOV):** 137.7

## Key Insights
- The business generated approximately **13.6M** in total revenue from **99K+ orders**.
- The average order value is **137.7**.
- Customer retention is very low:
  - **93,099** one-time customers
  - **2,997** repeat customers
- One-time customers contribute the majority of revenue, but repeat customers are more valuable per customer.
- Top revenue-generating categories are:
  - **Health & Beauty**
  - **Watches & Gifts**
  - **Bed, Bath & Table**
- Monthly revenue trends show growth initially, with a decline in later periods likely due to incomplete recent-month data.

## Business Recommendations
- Improve customer retention with loyalty and remarketing campaigns
- Encourage second purchases through personalized offers
- Focus promotions on high-performing categories
- Increase basket size using bundles and cross-sell strategies

## Python Visuals

### Monthly Revenue Trend
![Monthly Revenue Trend](visuals/monthly_revenue.png)

### Top Categories by Revenue
![Top Categories](visuals/top_categories.png)

### Customer Type Distribution
![Customer Type](visuals/customer_type.png)

## Folder Structure
ecommerce-customer-intelligence/
│
├── data/
├── sql/
├── python/
│   └── ecommerce_analysis.py
├── visuals/
├── README.md


Future Improvements
Build an interactive Power BI dashboard
Add cohort retention analysis
Perform customer segmentation (RFM)
Author

Mohammad Reyaz Shaik


