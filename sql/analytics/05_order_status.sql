-- Order Status Analysis

SELECT
    order_status,
    COUNT(*) AS total_orders,
    SUM(quantity) AS total_units
FROM staging_orders
GROUP BY order_status
ORDER BY total_orders DESC;