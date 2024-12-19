import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from visualizer import Visualizer
from utils import load_json_data, save_json_data
from sales_analyzer import SalesAnalyzer
from inventory_manager import InventoryManager
from product import Product
from ingredient import Ingredient
from sale import Sale
from user import User


class CoffeeShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Система склада кофейни")

        # Загрузка данных
        self.products = [Product(**p) for p in load_json_data('products.json')]
        self.ingredients = [Ingredient(**i) for i in load_json_data('ingredients.json')]
        self.sales = [Sale(**s) for s in load_json_data('sales_data.json')]
        self.users = load_json_data('users.json')

        # Инициализация атрибутов
        self.current_user = None
        self.analyzer = SalesAnalyzer(self.sales, self.products)
        self.inventory_manager = InventoryManager(self.products, self.ingredients, self.sales)
        self.visualizer = Visualizer()

        self.create_login_screen()

    def create_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Система склада кофейни", font=("Verdana", 18)).pack(pady=20)

        tk.Label(self.root, text="Имя пользователя:").pack()
        self.username_entry = tk.Entry(self.root)  # Сохраняем ссылку на новый объект Entry
        self.username_entry.pack()

        tk.Label(self.root, text="Пароль:").pack()
        self.password_entry = tk.Entry(self.root, show="*")  # Сохраняем ссылку на новый объект Entry
        self.password_entry.pack()

        tk.Button(self.root, text="Войти", command=self.handle_login).pack(pady=10)
        tk.Button(self.root, text="Выход", command=self.root.quit).pack(pady=10)

    def handle_login(self):
        username = self.username_entry.get().strip()  # Убираем лишние пробелы
        password = self.password_entry.get().strip()

        for user in self.users:
            if user['username'] == username and user['password'] == password:
                print(f"Найден пользователь: {user}")  # Отладка
                self.current_user = User(**user)
                self.show_main_interface()
                return

        messagebox.showerror("Ошибка", "Неправильный логин или пароль!")

    def show_main_interface(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Добро пожаловать, {self.current_user.username}", font=("Arial", 16)).pack(
            pady=10)

        if self.current_user.role == "admin":
            self.create_admin_interface()
        elif self.current_user.role == "manager":
            self.create_marketing_manager_interface()
        elif self.current_user.role == "cashier":
            self.create_procurement_manager_interface()
        else:
            messagebox.showerror("Ошибка", "Неизвестная роль!")
            self.create_login_screen()

    def create_admin_interface(self):
        tk.Button(self.root, text="График популярности", command=self.show_popularity_graph).pack(
            pady=5)
        tk.Button(self.root, text="График потребностей в инвентаре",
                  command=self.show_inventory_graph).pack(pady=5)
        tk.Button(self.root, text="Добавить нового пользователя", command=self.register_new_user).pack(
            pady=5)
        tk.Button(self.root, text="Удалить пользователя", command=self.delete_user).pack(pady=5)
        tk.Button(self.root, text="Выход", command=self.create_login_screen).pack(pady=10)

    def create_marketing_manager_interface(self):
        tk.Button(self.root, text="График популярности", command=self.show_popularity_graph).pack(
            pady=5)
        tk.Button(self.root, text="Экспорт отчета о продажах", command=self.export_sales_report).pack(
            pady=5)
        tk.Button(self.root, text="Выход", command=self.create_login_screen).pack(pady=10)

    def create_procurement_manager_interface(self):
        tk.Button(self.root, text="График потребностей в инвентаре",
                  command=self.show_inventory_graph).pack(pady=5)
        tk.Button(self.root, text="Экспорт отчета запасов", command=self.export_inventory_report).pack(
            pady=5)
        tk.Button(self.root, text="Выход", command=self.create_login_screen).pack(pady=10)

    def show_popularity_graph(self):
        if self.current_user.role not in ["admin", "manager"]:
            messagebox.showerror("Доступ запрещен", "У вас нет разрешения на просмотр этого графика.")
            return

        product_sales = self.analyzer.analyze_popularity()
        print(product_sales)  # Выводим DataFrame в консоль

        # Убедитесь, что здесь вы передаете правильные данные для визуализации
        fig = self.visualizer.plot_popularity(product_sales, show=False)
        self.display_graph(fig)

    def show_inventory_graph(self):
        if self.current_user.role not in ["admin", "cashier"]:
            messagebox.showerror("Доступ запрещен", "У вас нет разрешения на просмотр этого графика.")
            return

        low_stock_df = self.inventory_manager.analyze_inventory_needs()
        print(low_stock_df)  # Выводим DataFrame в консоль
        if low_stock_df.empty:
            messagebox.showinfo("Инфо", "Все ингредиенты в достаточном количестве.")
            return

        fig = self.visualizer.plot_inventory(low_stock_df, show=False)
        if fig is not None:
            self.display_graph(fig)

    def display_graph(self, fig):
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Граф")

        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def export_sales_report(self):
        product_sales = self.analyzer.analyze_popularity()
        print(product_sales)  # Выводим DataFrame в консоль
        if not product_sales.empty:  # Проверяем, есть ли данные для экспорта
            self.export_to_excel(product_sales, "sales_report.xlsx")
        else:
            messagebox.showwarning("Предупреждение", "Нет данных для экспорта отчета о продажах.")

    def export_inventory_report(self):
        low_stock_df = self.inventory_manager.analyze_inventory_needs()
        print(low_stock_df)  # Выводим DataFrame в консоль
        if not low_stock_df.empty:  # Проверяем, есть ли данные для экспорта
            self.export_to_excel(low_stock_df, "inventory_report.xlsx")
        else:
            messagebox.showwarning("Предупреждение", "Нет данных для экспорта отчета о пополнении запасов.")

    @staticmethod
    def export_to_excel(df, filename):
        try:
            df.to_excel(filename, index=False)
            messagebox.showinfo("Успех", f"Отчет экспортирован в {filename}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось экспортировать отчет: {e}")

    def register_new_user(self):
        def save_new_user():
            username = username_entry.get()
            password = password_entry.get()
            role = role_combobox.get()

            if not username or not password or not role:
                messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
                return

            self.users.append({"username": username, "password": password, "role": role})
            save_json_data('users.json', self.users)
            messagebox.showinfo("Успешно", "Новый пользователь добавлен!")
            register_window.destroy()

        register_window = tk.Toplevel(self.root)
        register_window.title("Добавить нового пользователя")

        tk.Label(register_window, text="Логин:").grid(row=0, column=0, padx=5, pady=5)
        username_entry = tk.Entry(register_window)
        username_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(register_window, text="Пароль:").grid(row=1, column=0, padx=5, pady=5)
        password_entry = tk.Entry(register_window, show="*")
        password_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(register_window, text="Роль:").grid(row=2, column=0, padx=5, pady=5)
        role_combobox = ttk.Combobox(register_window, values=["admin", "manager", "cashier"])
        role_combobox.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(register_window, text="Добавить", command=save_new_user).grid(row=3, column=0, columnspan=2, pady=10)

    def delete_user(self):
        if self.current_user.role != "admin":
            messagebox.showerror("Доступ запрещён", "У вас недостаточно прав, чтобы удалить пользователя из системы.")
            return

        delete_window = tk.Toplevel(self.root)
        delete_window.title("Удаление пользователя")

        tk.Label(delete_window, text="Логин пользователя:").grid(row=0, column=0, padx=5, pady=5)
        username_entry = tk.Entry(delete_window)
        username_entry.grid(row=0, column=1, padx=5, pady=5)

        def confirm_delete():
            username = username_entry.get()
            for user in self.users:
                if user['username'] == username:
                    if user['role'] == "admin":
                        messagebox.showerror("Ошибка", "Невозможно удалить аккаунт администратора.")
                        return
                    self.users.remove(user)
                    save_json_data('users.json', self.users)
                    messagebox.showinfo("Успешно", f"Пользователь '{username}' успешно удален.")
                    delete_window.destroy()
                    return
            messagebox.showerror("Ошибка", f"Пользователь '{username}' не найден.")

        def cancel_action():
            delete_window.destroy()  # Закрываем окно удаления пользователя

        tk.Button(delete_window, text="Удалить", command=confirm_delete).grid(row=1, column=0, pady=10, padx=5)
        tk.Button(delete_window, text="Отмена", command=cancel_action).grid(row=1, column=1, pady=10, padx=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeShopApp(root)
    root.mainloop()
