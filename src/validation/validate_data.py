import pandas as pd


def validate_customers(df):
    required_columns = [
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "country",
        "city",
        "signup_date"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column in customers data: {column}")

    if df["customer_id"].duplicated().any():
        raise ValueError("Duplicate customer_id found.")

    if df["customer_id"].isnull().any():
        raise ValueError("Missing customer_id found.")

    return True


def validate_products(df):
    required_columns = [
        "product_id",
        "product_name",
        "category",
        "price",
        "cost"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column in products data: {column}")

    if df["product_id"].duplicated().any():
        raise ValueError("Duplicate product_id found.")

    if df["price"].isnull().any():
        raise ValueError("Missing product price found.")

    if (df["price"] < 0).any():
        raise ValueError("Negative product price found.")

    if (df["cost"] < 0).any():
        raise ValueError("Negative product cost found.")

    return True


def validate_orders(df):
    required_columns = [
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "payment_method",
        "order_status"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column in orders data: {column}")

    if df["order_id"].duplicated().any():
        raise ValueError("Duplicate order_id found.")

    if df["order_id"].isnull().any():
        raise ValueError("Missing order_id found.")

    if (df["quantity"] <= 0).any():
        raise ValueError("Invalid order quantity found.")

    return True


def validate_api_products(df):
    required_columns = [
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

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(
                f"Missing column in API products data: {column}"
            )

    if df["id"].duplicated().any():
        raise ValueError("Duplicate API product id found.")

    if df["id"].isnull().any():
        raise ValueError("Missing API product id found.")

    if df["price"].isnull().any():
        raise ValueError("Missing API product price found.")

    if (df["price"] < 0).any():
        raise ValueError("Negative API product price found.")

    if (df["stock"] < 0).any():
        raise ValueError("Negative API product stock found.")

    return True