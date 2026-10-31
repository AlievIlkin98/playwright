import re
import pytest
from playwright.sync_api import Page, expect

from pages.registration_page import RegistrationPage


# Задаем кортеж с параметрами: "email, username, password"
@pytest.mark.parametrize(
    "email, username, password",
    [
        ("test_user1@example.com", "user_one", "SecurePass123")
    ],
)
def test_registration(page: Page, email, username, password):
    # 1. Инициализируем страницу
    registration_page = RegistrationPage(page)

    # 2. Переходим на сайт
    registration_page.navigate()

    # 3. Регистрируем пользователя (данные берутся из параметров)
    registration_page.register(email, username, password)

    # 4. Проверяем, что после регистрации нас перекинуло на дашборд
    expect(page).to_have_url(re.compile(r"#/dashboard$"))
