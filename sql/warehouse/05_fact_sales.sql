-- ============================================================
-- E-Commerce Data Warehouse
-- Step 18.5 - Sales Fact Table
-- ============================================================

-- Create Sales Fact Table

CREATE TABLE warehouse.fact_sales (
    sales_key SERIAL PRIMARY KEY,
    order_id VARCHAR(10) NOT NULL,

    customer_key INTEGER NOT NULL,
    product_key INTEGER NOT NULL,
    date_key INTEGER NOT NULL,

    quantity INTEGER,
    payment_method VARCHAR(50),
    order_status VARCHAR(50),

    unit_price NUMERIC(10,2),
    unit_cost NUMERIC(10,2),

    revenue NUMERIC(12,2),
    profit NUMERIC(12,2),

    -- Foreign Keys

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_key)
        REFERENCES warehouse.dim_customer(customer_key),

    CONSTRAINT fk_product
        FOREIGN KEY (product_key)
        REFERENCES warehouse.dim_product(product_key),

    CONSTRAINT fk_date
        FOREIGN KEY (date_key)
        REFERENCES warehouse.dim_date(date_key)
);

-- ============================================================
-- Load Sales Data
-- ============================================================

INSERT INTO warehouse.fact_sales (
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
)
SELECT
    o.order_id,
    c.customer_key,
    p.product_key,
    d.date_key,

    o.quantity,
    o.payment_method,
    o.order_status,

    p.price AS unit_price,
    p.cost AS unit_cost,

    p.price * o.quantity AS revenue,

    (p.price - p.cost) * o.quantity AS profit

FROM staging_orders o

JOIN warehouse.dim_customer c
    ON o.customer_id = c.customer_id

JOIN warehouse.dim_product p
    ON o.product_id = p.product_id

JOIN warehouse.dim_date d
    ON o.order_date = d.full_date;