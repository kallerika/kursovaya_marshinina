import pandas as pd

class SalesAnalyzer:
    def __init__(self, sales, products):
        self.sales = sales
        self.products = products

    def analyze_popularity(self):
        # Преобразуем данные о продажах в DataFrame
        if not self.sales:
            raise ValueError("Данные о продажах некорректны или отсутствуют.")

        try:
            sales_df = pd.DataFrame([vars(sale) for sale in self.sales])
        except Exception as e:
            raise ValueError(f"Не удалось преобразовать данные о продажах в DataFrame: {e}")

        # Проверяем наличие необходимых колонок
        if 'product_id' not in sales_df.columns or 'sold_units' not in sales_df.columns:
            raise KeyError("DataFrame не нашел ключевые столбцы: 'product_id' или 'sold_units'")

        # Приведение типов
        sales_df['product_id'] = sales_df['product_id'].astype(str)
        product_df = pd.DataFrame([vars(product) for product in self.products])
        product_df['product_id'] = product_df['product_id'].astype(str)

        # Группируем продажи по product_id
        product_sales = sales_df.groupby('product_id')['sold_units'].sum().reset_index()

        # Объединяем с DataFrame продуктов
        product_sales = product_sales.merge(product_df[['product_id', 'product_name']], on='product_id')

        # Выбираем только нужные колонки
        product_sales = product_sales[['product_name', 'sold_units']]
        product_sales.columns = ['Товар', 'Проданных единиц']

        # Возвращаем данные, отсортированные по количеству продаж
        return product_sales.sort_values(by='Проданных единиц', ascending=False)
