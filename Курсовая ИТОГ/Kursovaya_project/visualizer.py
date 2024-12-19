import matplotlib.pyplot as plt


class Visualizer:
    @staticmethod
    def plot_popularity(product_sales, sort_by='Проданных единиц', color='plum', show=True):
        # Проверяем, что DataFrame не пустой
        if product_sales.empty:
            print("Нет данных для отображения популярности продуктов.")
            return None

        # Сортируем данные для визуализации
        product_sales = product_sales.sort_values(by=sort_by, ascending=False)

        # Построение графика
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(product_sales['Товар'], product_sales['Проданных единиц'], color=color)
        ax.set_title('Популярность продуктов')
        ax.set_xlabel('Количество проданных единиц')
        ax.set_ylabel('Продукты')

        # Добавляем подписи на график
        for bar in bars:
            ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
                    f'{bar.get_width()}', va='center', ha='left')

        plt.tight_layout()
        if show:
            plt.show()
        return fig  # Возвращаем объект Figure для отображения в Tkinter

    @staticmethod
    def plot_inventory(low_stock_df, color='powderblue', show=True):
        if low_stock_df.empty or (low_stock_df['Необходимое количество'] <= 0).all():
            print("Все ингредиенты в достаточном количестве.")
            return None  # Возвращаем None, если график не требуется.

        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(low_stock_df['Ингредиент'], low_stock_df['Необходимое количество'], color=color)
        ax.set_title('Необходимость пополнения ингредиентов')
        ax.set_xlabel('Требуемое количество')
        ax.set_ylabel('Ингредиенты')

        for bar in bars:
            ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
                    f'{bar.get_width()}', va='center', ha='left')

        plt.tight_layout()
        if show:
            plt.show()
        return fig  # Возвращаем объект Figure.
