-- Top Categories

SELECT 
    ct.product_category_name_english AS category,
    SUM(oi.price) AS total_revenue,
    COUNT(*) AS total_orders
FROM order_items oi
JOIN products p 
    ON oi.product_id = p.product_id
JOIN category_translation ct 
    ON p.product_category_name = ct.product_category_name
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 10;

