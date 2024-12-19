import pytest
from tkinter import Tk
from main import CoffeeShopApp


@pytest.fixture
def app():
    root = Tk()
    app = CoffeeShopApp(root)
    return app


def test_login_success(app):
    app.username_entry.insert(0, "admin")
    app.password_entry.insert(0, "admin")
    app.handle_login()
    assert app.current_user is not None  # Проверка успешного входа


def test_login_failure(app):
    app.username_entry.insert(0, "wrong_user")
    app.password_entry.insert(0, "wrong_password")
    app.handle_login()
    assert app.current_user is None  # Проверка на отсутствие пользователя
