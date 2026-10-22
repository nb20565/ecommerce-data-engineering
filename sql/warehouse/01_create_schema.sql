-- ============================================================
-- E-Commerce Data Warehouse
-- Step 18.2 - Customer Dimension
-- ============================================================

CREATE TABLE warehouse.dim_customer (
    customer_key SERIAL PRIMARY KEY,
    customer_id VARCHAR(10) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    country VARCHAR(100),
    city VARCHAR(100),
    signup_date DATE
);

-- Load data from staging

INSERT INTO warehouse.dim_customer (
    customer_id,
    first_name,
    last_name,
    email,
    country,
    city,
    signup_date
)
SELECT
    customer_id,
    first_name,
    last_name,
    email,
    country,
    city,
    signup_date
FROM staging_customers;