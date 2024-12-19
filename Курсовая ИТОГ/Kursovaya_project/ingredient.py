class Ingredient:
    def __init__(self, ingredient_id, ingredient_name, stock_quantity):
        self.ingredient_id = ingredient_id
        self.ingredient_name = ingredient_name
        self.stock_quantity = stock_quantity

    def update_stock(self, amount):
        self.stock_quantity += amount

    def to_dict(self):
        return {
            "ingredient_id": self.ingredient_id,
            "ingredient_name": self.ingredient_name,
            "stock_quantity": self.stock_quantity
        }
