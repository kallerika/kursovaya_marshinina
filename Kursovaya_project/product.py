class Product:
    def __init__(self, product_id, product_name, stock_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.product_name} ({self.product_id})"

    def __repr__(self):
        return f"""
        Товары
        (product_id = {self.product_id},
        product_name = {self.product_name},
        stock_quantity = {self.stock_quantity})
        """
