import json
from product import Product
from sale import Sale
from inventory_manager import InventoryManager
from sales_analyzer import SalesAnalyzer
from visualizer import Visualizer


# Загрузка данных из JSON
def load_json_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def main():
    # Загрузка данных
    products_data = load_json_data('products.json')
    sales_data = load_json_data('sales_data.json')

    if not sales_data or not products_data:
        print("Нет данных для анализа.")
        return

    # Создание объектов для продуктов и продаж
    products = [Product(**p) for p in products_data]
    sales = [Sale(**s) for s in sales_data]

    # Анализ популярности продуктов
    analyzer = SalesAnalyzer(sales, products)
    product_sales = analyzer.analyze_popularity()
    print("Анализ популярности продуктов:")
    print(product_sales)

    # Визуалка популярности продуктов
    visualizer = Visualizer()
    visualizer.plot_popularity(product_sales)

    # Анализ пополнения запасов
    inventory_manager = InventoryManager(products, sales)
    low_stock_products = inventory_manager.analyze_inventory_needs()
    print("\nПродукты, которые требуют пополнения запасов:")
    print(low_stock_products)

    # Визуалка пополнения запасов
    visualizer.plot_inventory(low_stock_products)


if __name__ == "__main__":
    main()
