import pandas as pd


class InventoryManager:
    def __init__(self, products, ingredients, sales):
        self.products = products
        self.ingredients = ingredients
        self.sales = sales

    def analyze_inventory_needs(self):
        sales_by_product = {sale.product_id: sale.sold_units for sale in self.sales}
        ingredient_needs = {ingredient.ingredient_id: 0 for ingredient in self.ingredients}

        for product in self.products:
            product_sales = sales_by_product.get(product.product_id, 0)
            for ingredient_id, amount_needed in product.ingredient_requirements.items():
                ingredient_needs[ingredient_id] += amount_needed * product_sales

        low_stock_ingredients = []
        for ingredient in self.ingredients:
            required_stock = ingredient_needs[ingredient.ingredient_id] - ingredient.stock_quantity
            if required_stock > 0:
                low_stock_ingredients.append((ingredient.ingredient_name, required_stock))

        df = pd.DataFrame(low_stock_ingredients, columns=['Ингредиент', 'Необходимое количество'])
        return df
