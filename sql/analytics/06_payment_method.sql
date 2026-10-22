-- Payment Method Analysis

SELECT
    payment_method,
    COUNT(*) AS total_orders,
    SUM(o.quantity) AS total_units,
    SUM(p.price * o.quantity) AS total_revenue
FROM staging_orders o
JOIN staging_products p
    ON o.product_id = p.product_id
WHERE o.order_status = 'Completed'
GROUP BY payment_method
ORDER BY total_revenue DESC;