import json
import logging
import os

import pandas as pd
import requests
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from src.validation.validate_data import validate_api_products


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


API_URL = "https://dummyjson.com/products"

OUTPUT_FILE = "data/raw/api_products.json"
PROCESSED_FILE = "data/processed/api_products_cleaned.csv"

def save_processed_products(df):
    os.makedirs(os.path.dirname(PROCESSED_FILE), exist_ok=True)

    df.to_csv(PROCESSED_FILE, index=False)

    logger.info(
        f"Processed API data saved to: {PROCESSED_FILE}"
    )


def fetch_products_from_api():
    logger.info("Starting API request...")

    response = requests.get(API_URL, timeout=30)

    response.raise_for_status()

    data = response.json()

    products = data.get("products", [])

    logger.info(f"Products received from API: {len(products)}")

    return products


def save_products_to_json(products):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4)

    logger.info(f"API data saved to: {OUTPUT_FILE}")


def transform_products_to_dataframe(products):
    df = pd.DataFrame(products)

    selected_columns = [
        "id",
        "title",
        "category",
        "price",
        "discountPercentage",
        "rating",
        "stock",
        "brand",
        "sku"
    ]

    df = df[selected_columns]

    logger.info(
        f"API products transformed into DataFrame: {df.shape}"
    )

    return df


if __name__ == "__main__":
    products = fetch_products_from_api()

    save_products_to_json(products)

    products_df = transform_products_to_dataframe(products)

    logger.info("Starting API data validation...")

    validate_api_products(products_df)

    logger.info("API products validation passed.")

    save_processed_products(products_df)

    print("\nDataFrame shape:")
    print(products_df.shape)

    print("\nDataFrame columns:")
    print(products_df.columns.tolist())

    print("\nFirst 3 rows:")
    print(products_df.head(3))