import pytest
from inventory_manager import InventoryManager
from sales_analyzer import SalesAnalyzer
from product import Product
from sale import Sale
from ingredient import Ingredient


@pytest.fixture
def setup_inventory_system():
    products = [Product("1", "Капучино", 10, {"1": 1, "2": 2})]
    ingredients = [Ingredient("1", "Кофе", 50), Ingredient("2", "Молоко", 20)]  # Добавляем ингредиенты
    sales = [Sale("1", 5)]
    inventory_manager = InventoryManager(products, ingredients, sales)  # Передаем ингредиенты
    sales_analyzer = SalesAnalyzer(sales, products)
    return inventory_manager, sales_analyzer


def test_inventory_needs_analysis(setup_inventory_system):
    inventory_manager, _ = setup_inventory_system
    low_stock_df = inventory_manager.analyze_inventory_needs()
    assert len(low_stock_df) == 0


def test_sales_analysis(setup_inventory_system):
    _, sales_analyzer = setup_inventory_system
    product_sales = sales_analyzer.analyze_popularity()
    assert product_sales['Товар'][0] == "Капучино"  # Проверка на популярность товара
