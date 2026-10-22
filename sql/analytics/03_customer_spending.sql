-- Top Customers by Spending

SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.country,
    SUM(p.price * o.quantity) AS total_spent
FROM staging_orders o
JOIN staging_customers c
    ON o.customer_id = c.customer_id
JOIN staging_products p
    ON o.product_id = p.product_id
WHERE o.order_status = 'Completed'
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.country
ORDER BY total_spent DESC;