-- Customer Type Analysis

SELECT 
    customer_type,
    COUNT(*) AS customer_count
FROM (
    SELECT 
        customer_unique_id,
        COUNT(DISTINCT o.order_id) AS total_orders,
        CASE 
            WHEN COUNT(DISTINCT o.order_id) = 1 THEN 'One-Time'
            ELSE 'Repeat'
        END AS customer_type
    FROM customers c
    JOIN orders o 
        ON c.customer_id = o.customer_id
    GROUP BY customer_unique_id
) t
GROUP BY customer_type;