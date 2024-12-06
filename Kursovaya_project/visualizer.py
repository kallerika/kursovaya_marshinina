import matplotlib.pyplot as plt


class Visualizer:
    @staticmethod
    def plot_popularity(product_sales, sort_by='sold_units', color='plum'):
        """
        График популярности продуктов
        product_sales: данные о продажах продуктов в виде DataFrame
        sort_by: сортировка по столбц
        color: цвет столбцов
        """
        product_sales = product_sales.sort_values(by=sort_by, ascending=False)

        plt.figure(figsize=(10, 6))
        bars = plt.barh(product_sales['product_name'], product_sales['sold_units'], color=color)
        plt.title('Популярность продуктов')
        plt.xlabel('Количество проданных единиц')
        plt.ylabel('Продукты')

        for bar in bars:
            plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
                     f'{bar.get_width()}', va='center', ha='left', color='black')

        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_inventory(low_stock_df, color='powderblue'):
        """
        График потребности в пополнении запасов
        low_stock_df: данные о товарах, требующих пополнения в виде DataFrame
        color: цвет столбцов
        """
        if low_stock_df.empty:
            print("Все товары в достаточном количестве.")
            return

        plt.figure(figsize=(10, 6))
        bars = plt.barh(low_stock_df['Название'], low_stock_df['Необходимый запас'], color=color)
        plt.title('Необходимость пополнения запасов')
        plt.xlabel('Необходимое количество для пополнения')
        plt.ylabel('Продукты')

        for bar in bars:
            plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
                     f'{bar.get_width()}', va='center', ha='left', color='black')

        plt.tight_layout()
        plt.show()
