class Product:
    def __init__(self, product_id, product_name, stock_quantity, ingredient_requirements):
        self.product_id = product_id
        self.product_name = product_name
        self.stock_quantity = stock_quantity
        self.ingredient_requirements = ingredient_requirements

    def update_stock(self, amount):
        self.stock_quantity += amount

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "stock_quantity": self.stock_quantity,
            "ingredient_requirements": self.ingredient_requirements
        }
