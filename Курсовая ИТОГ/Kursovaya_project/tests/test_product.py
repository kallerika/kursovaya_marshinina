import pytest
from product import Product


@pytest.fixture
def product():
    return Product(product_id="1", product_name="Капучино", stock_quantity=10, ingredient_requirements={"1": 1, "2": 2})


def test_initialization(product):
    assert product.product_id == "1"
    assert product.product_name == "Капучино"
    assert product.stock_quantity == 10


def test_update_stock(product):
    product.update_stock(5)
    assert product.stock_quantity == 15


def test_to_dict(product):
    expected_dict = {
        "product_id": "1",
        "product_name": "Капучино",
        "stock_quantity": 10,
        "ingredient_requirements": {"1": 1, "2": 2}
    }
    assert product.to_dict() == expected_dict
