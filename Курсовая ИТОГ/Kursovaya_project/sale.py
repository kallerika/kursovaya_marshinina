class Sale:
    def __init__(self, product_id, sold_units):
        self.product_id = product_id
        self.sold_units = sold_units

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "sold_units": self.sold_units,
        }
