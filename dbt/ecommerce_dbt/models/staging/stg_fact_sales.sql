{{ config(materialized='view') }}

SELECT
    sales_key,
    order_id,
    customer_key,
    product_key,
    date_key,
    quantity,
    payment_method,
    order_status,
    unit_price,
    unit_cost,
    revenue,
    profit
FROM warehouse.fact_sales