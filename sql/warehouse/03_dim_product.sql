-- ============================================================
-- E-Commerce Data Warehouse
-- Step 18.3 - Product Dimension
-- ============================================================

-- Create Product Dimension Table

CREATE TABLE warehouse.dim_product (
    product_key SERIAL PRIMARY KEY,
    product_id VARCHAR(10) NOT NULL,
    product_name VARCHAR(255),
    category VARCHAR(100),
    price NUMERIC(10,2),
    cost NUMERIC(10,2)
);

-- Load products from staging table

INSERT INTO warehouse.dim_product (
    product_id,
    product_name,
    category,
    price,
    cost
)
SELECT
    product_id,
    product_name,
    category,
    price,
    cost
FROM staging_products;