import pandas as pd


class InventoryManager:
    def __init__(self, products, sales):
        self.products = products
        self.sales = sales

    def analyze_inventory_needs(self):
        sales_by_product = {sale.product_id: sale.sold_units for sale in self.sales}

        low_stock = []

        for product in self.products:
            required_stock = sales_by_product.get(product.product_id, 0) + 10 - product.stock_quantity
            if required_stock > 0:
                low_stock.append((product.product_name, required_stock))

        df = pd.DataFrame(low_stock, columns=['Название', 'Необходимый запас'])
        return df
