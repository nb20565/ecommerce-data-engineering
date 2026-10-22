-- Step 17: Sales Summary
-- Total Revenue

SELECT
    SUM(p.price * o.quantity) AS total_revenue
FROM staging_orders o
JOIN staging_products p
    ON o.product_id = p.product_id
WHERE o.order_status = 'Completed';


-- Total Profit

SELECT
    SUM((p.price - p.cost) * o.quantity) AS total_profit
FROM staging_orders o
JOIN staging_products p
    ON o.product_id = p.product_id
WHERE o.order_status = 'Completed';