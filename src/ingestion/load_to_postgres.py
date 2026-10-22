import os
from urllib.parse import quote_plus

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


# ============================================
# 1. Load environment variables
# ============================================

load_dotenv()


# ============================================
# 2. Read PostgreSQL settings from .env
# ============================================

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# ============================================
# 3. Check required settings
# ============================================

if not DB_HOST:
    raise ValueError("DB_HOST is missing from .env")

if not DB_PORT:
    raise ValueError("DB_PORT is missing from .env")

if not DB_NAME:
    raise ValueError("DB_NAME is missing from .env")

if not DB_USER:
    raise ValueError("DB_USER is missing from .env")

if not DB_PASSWORD:
    raise ValueError("DB_PASSWORD is missing from .env")


# ============================================
# 4. Encode password
# ============================================
# This is important because your password contains @.
# quote_plus() safely handles @, #, %, !, etc.

encoded_password = quote_plus(DB_PASSWORD)


# ============================================
# 5. Create PostgreSQL connection
# ============================================

connection_url = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{encoded_password}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(connection_url)


# ============================================
# 6. CSV file paths
# ============================================

customers_file = "data/processed/customers_cleaned.csv"
products_file = "data/processed/products_cleaned.csv"
orders_file = "data/processed/orders_cleaned.csv"


# ============================================
# 7. Read CSV files
# ============================================

customers = pd.read_csv(customers_file)
products = pd.read_csv(products_file)
orders = pd.read_csv(orders_file)

print("CSV files loaded successfully.")


# ============================================
# 8. Load customers
# ============================================

customers.to_sql(
    "staging_customers",
    engine,
    if_exists="append",
    index=False
)

print(f"Customers loaded: {len(customers)}")


# ============================================
# 9. Load products
# ============================================

products.to_sql(
    "staging_products",
    engine,
    if_exists="append",
    index=False
)

print(f"Products loaded: {len(products)}")


# ============================================
# 10. Load orders
# ============================================

orders.to_sql(
    "staging_orders",
    engine,
    if_exists="append",
    index=False
)

print(f"Orders loaded: {len(orders)}")


# ============================================
# 11. Final message
# ============================================

print("Data successfully loaded into PostgreSQL!")