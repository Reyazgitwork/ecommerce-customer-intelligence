-- Revenue by Customer Type

SELECT 
    customer_type,
    SUM(oi.price) AS total_revenue
FROM (
    SELECT 
        c.customer_unique_id,
        o.order_id,
        CASE 
            WHEN COUNT(o.order_id) OVER (PARTITION BY c.customer_unique_id) = 1 
            THEN 'One-Time'
            ELSE 'Repeat'
        END AS customer_type
    FROM customers c
    JOIN orders o 
        ON c.customer_id = o.customer_id
) t
JOIN order_items oi 
    ON t.order_id = oi.order_id
GROUP BY customer_type;