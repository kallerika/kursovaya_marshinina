class Sale:
    def __init__(self, product_id, sold_units):
        self.product_id = product_id
        self.sold_units = sold_units

    def __str__(self):
        return f"Продажи {self.product_id}, всего продано: {self.sold_units}"

    def __repr__(self):
        return f"""
        Продажи
        (product_id = {self.product_id},
        sold_units = {self.sold_units})
        """
