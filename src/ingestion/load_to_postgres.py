import logging
import os
import sys
from urllib.parse import quote_plus

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# ============================================================
# Logging Configuration
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


# Allow imports from the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.validation.validate_data import (
    validate_customers,
    validate_products,
    validate_orders,
)


# ============================================================
# 1. Load environment variables
# ============================================================

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# ============================================================
# 2. Validate database configuration
# ============================================================

required_variables = {
    "DB_HOST": DB_HOST,
    "DB_PORT": DB_PORT,
    "DB_NAME": DB_NAME,
    "DB_USER": DB_USER,
    "DB_PASSWORD": DB_PASSWORD,
}

for variable, value in required_variables.items():
    if not value:
        raise ValueError(f"{variable} is missing from .env")


# ============================================================
# 3. Create PostgreSQL connection
# ============================================================

encoded_password = quote_plus(DB_PASSWORD)

connection_url = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{encoded_password}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(connection_url)

logger.info("Database connection configured successfully.")


# ============================================================
# 4. Load cleaned CSV files
# ============================================================

customers_file = "data/processed/customers_cleaned.csv"
products_file = "data/processed/products_cleaned.csv"
orders_file = "data/processed/orders_cleaned.csv"

customers = pd.read_csv(customers_file)
products = pd.read_csv(products_file)
orders = pd.read_csv(orders_file)

logger.info("CSV files loaded successfully.")

logger.info(f"Customers: {len(customers)}")
logger.info(f"Products: {len(products)}")
logger.info(f"Orders: {len(orders)}")


# ============================================================
# 5. Validate data
# ============================================================

logger.info("Starting data validation...")

validate_customers(customers)
logger.info("Customers validation passed.")

validate_products(products)
logger.info("Products validation passed.")

validate_orders(orders)
logger.info("Orders validation passed.")


# ============================================================
# 6. Load data into PostgreSQL
# ============================================================

logger.info("Loading data into PostgreSQL...")


# Clear existing staging data

with engine.begin() as connection:
    connection.exec_driver_sql(
        "TRUNCATE TABLE staging_orders, staging_products, staging_customers "
        "RESTART IDENTITY CASCADE"
    )

logger.info("Existing staging data cleared.")


# Load customers

customers.to_sql(
    "staging_customers",
    engine,
    if_exists="append",
    index=False
)

logger.info(f"Customers loaded: {len(customers)}")


# Load products

products.to_sql(
    "staging_products",
    engine,
    if_exists="append",
    index=False
)

logger.info(f"Products loaded: {len(products)}")


# Load orders

orders.to_sql(
    "staging_orders",
    engine,
    if_exists="append",
    index=False
)

logger.info(f"Orders loaded: {len(orders)}")

# ============================================================
# 7. Pipeline completed
# ============================================================

logger.info("ETL pipeline completed successfully!")