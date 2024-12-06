import pandas as pd


class SalesAnalyzer:
    def __init__(self, sales, products):
        self.sales = sales
        self.products = products

    def analyze_popularity(self):
        sales_df = pd.DataFrame([vars(sale) for sale in self.sales])
        product_sales = sales_df.groupby('product_id')['sold_units'].sum().reset_index()
        product_sales = product_sales.merge(pd.DataFrame([vars(product) for product in self.products]),
                                            on='product_id')
        return product_sales.sort_values(by='sold_units', ascending=False)
