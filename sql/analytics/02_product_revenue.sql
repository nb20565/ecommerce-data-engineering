-- Revenue by Product

SELECT
    p.product_name,
    SUM(o.quantity) AS units_sold,
    SUM(p.price * o.quantity) AS revenue
FROM staging_orders o
JOIN staging_products p
    ON o.product_id = p.product_id
WHERE o.order_status = 'Completed'
GROUP BY p.product_name
ORDER BY revenue DESC;