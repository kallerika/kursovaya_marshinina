import pytest
from sales_analyzer import SalesAnalyzer
from product import Product
from sale import Sale

# Параметризуем данные для продуктов и продаж
@pytest.mark.parametrize(
    "products, sales, expected_first, expected_second, expected_last",
    [
        (
            [
                Product(1, "Латте", 90),
                Product(2, "Капучино", 75),
                Product(3, "Черный чай", 50),
                Product(4, "Двойной эспрессо", 10),
                Product(5, "Американо", 30)
            ],
            [
                Sale(1, 50),
                Sale(2, 70),
                Sale(3, 30),
                Sale(4, 5),
                Sale(5, 15)
            ],
            "Капучино",
            "Латте",        # Ожидаемые элементы
            "Двойной эспрессо"
        )
    ]
)
def test_analyze_popularity(products, sales, expected_first, expected_second, expected_last):
    analyzer = SalesAnalyzer(sales, products)
    result = analyzer.analyze_popularity()

    # Проверка, что результат отсортирован по проданным единицам (ascending='False')
    assert result.iloc[0]['product_name'] == expected_first
    assert result.iloc[1]['product_name'] == expected_second
    assert result.iloc[4]['product_name'] == expected_last

    # Проверка правильности данных
    assert result.iloc[0]['sold_units'] == 70
    assert result.iloc[1]['sold_units'] == 50
