{{ config(materialized='table') }}

SELECT
    customer_key,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS total_units,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit
FROM {{ ref('stg_fact_sales') }}
WHERE order_status = 'Completed'
GROUP BY customer_key
ORDER BY total_revenue DESC