import pytest
from product import Product

# Параметризуем данные для инициализации продукта
@pytest.mark.parametrize(
    "product_id, product_name, stock_quantity",
    [
        (1, "Латте", 90),
        (2, "Капучино", 75),
        (3, "Черный чай", 50),
        (4, "Двойной эспрессо", 10)
    ]
)
def test_product_initialization(product_id, product_name, stock_quantity):
    product = Product(product_id, product_name, stock_quantity)
    assert product.product_id == product_id
    assert product.product_name == product_name
    assert product.stock_quantity == stock_quantity

# Параметризуем данные для метода __str__
@pytest.mark.parametrize(
    "product_id, product_name, expected_str",
    [
        (1, "Латте", "Латте (1)"),
        (2, "Капучино", "Капучино (2)"),
        (3, "Черный чай", "Черный чай (3)"),
        (4, "Двойной эспрессо", "Двойной эспрессо (4)")
    ]
)
def test_product_str_method(product_id, product_name, expected_str):
    product = Product(product_id, product_name, 90)  # stock_quantity не влияет на __str__
    assert str(product) == expected_str
