import pandas as pd
import pytest

from src.validation.validate_data import (
    validate_customers,
    validate_products,
    validate_orders
)


def test_valid_customers():
    df = pd.DataFrame({
        "customer_id": ["C001"],
        "first_name": ["John"],
        "last_name": ["Smith"],
        "email": ["john@email.com"],
        "country": ["France"],
        "city": ["Paris"],
        "signup_date": ["2025-01-15"]
    })

    assert validate_customers(df) is True


def test_duplicate_customer_id():
    df = pd.DataFrame({
        "customer_id": ["C001", "C001"],
        "first_name": ["John", "Emma"],
        "last_name": ["Smith", "Johnson"],
        "email": ["john@email.com", "emma@email.com"],
        "country": ["France", "Germany"],
        "city": ["Paris", "Berlin"],
        "signup_date": ["2025-01-15", "2025-02-20"]
    })

    with pytest.raises(ValueError):
        validate_customers(df)


def test_valid_products():
    df = pd.DataFrame({
        "product_id": ["P001"],
        "product_name": ["Laptop"],
        "category": ["Electronics"],
        "price": [1200],
        "cost": [850]
    })

    assert validate_products(df) is True


def test_negative_product_price():
    df = pd.DataFrame({
        "product_id": ["P001"],
        "product_name": ["Laptop"],
        "category": ["Electronics"],
        "price": [-1200],
        "cost": [850]
    })

    with pytest.raises(ValueError):
        validate_products(df)


def test_valid_orders():
    df = pd.DataFrame({
        "order_id": ["O001"],
        "customer_id": ["C001"],
        "product_id": ["P001"],
        "order_date": ["2025-06-15"],
        "quantity": [1],
        "payment_method": ["Credit Card"],
        "order_status": ["Completed"]
    })

    assert validate_orders(df) is True


def test_invalid_order_quantity():
    df = pd.DataFrame({
        "order_id": ["O001"],
        "customer_id": ["C001"],
        "product_id": ["P001"],
        "order_date": ["2025-06-15"],
        "quantity": [0],
        "payment_method": ["Credit Card"],
        "order_status": ["Completed"]
    })

    with pytest.raises(ValueError):
        validate_orders(df)