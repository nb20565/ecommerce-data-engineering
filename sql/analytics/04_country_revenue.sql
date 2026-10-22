-- Revenue by Country

SELECT
    c.country,
    COUNT(DISTINCT o.customer_id) AS customers,
    SUM(o.quantity) AS units_sold,
    SUM(p.price * o.quantity) AS total_revenue
FROM staging_orders o
JOIN staging_customers c
    ON o.customer_id = c.customer_id
JOIN staging_products p
    ON o.product_id = p.product_id
WHERE o.order_status = 'Completed'
GROUP BY c.country
ORDER BY total_revenue DESC;