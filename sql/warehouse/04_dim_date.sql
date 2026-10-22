-- ============================================================
-- E-Commerce Data Warehouse
-- Step 18.4 - Date Dimension
-- ============================================================

-- Create Date Dimension Table

CREATE TABLE warehouse.dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date DATE NOT NULL,
    day INTEGER,
    month INTEGER,
    month_name VARCHAR(20),
    quarter INTEGER,
    year INTEGER,
    day_name VARCHAR(20),
    day_of_week INTEGER
);

-- Load Date Dimension

INSERT INTO warehouse.dim_date (
    date_key,
    full_date,
    day,
    month,
    month_name,
    quarter,
    year,
    day_name,
    day_of_week
)
SELECT
    CAST(TO_CHAR(
        CAST('2025-06-15' AS DATE) + day_number,
        'YYYYMMDD'
    ) AS INTEGER) AS date_key,

    CAST('2025-06-15' AS DATE) + day_number AS full_date,

    EXTRACT(
        DAY FROM CAST('2025-06-15' AS DATE) + day_number
    ) AS day,

    EXTRACT(
        MONTH FROM CAST('2025-06-15' AS DATE) + day_number
    ) AS month,

    TRIM(TO_CHAR(
        CAST('2025-06-15' AS DATE) + day_number,
        'Month'
    )) AS month_name,

    EXTRACT(
        QUARTER FROM CAST('2025-06-15' AS DATE) + day_number
    ) AS quarter,

    EXTRACT(
        YEAR FROM CAST('2025-06-15' AS DATE) + day_number
    ) AS year,

    TRIM(TO_CHAR(
        CAST('2025-06-15' AS DATE) + day_number,
        'Day'
    )) AS day_name,

    EXTRACT(
        ISODOW FROM CAST('2025-06-15' AS DATE) + day_number
    ) AS day_of_week

FROM generate_series(0, 14) AS day_number;