import re
import pytest
from playwright.sync_api import Browser, Page, expect


@pytest.fixture(scope="session")
def auth_state_path(browser: Browser, tmp_path_factory) -> str:
    """Выполняет регистрацию 1 раз за сессию и сохраняет куки + localStorage в JSON."""
    state_file = tmp_path_factory.mktemp("auth") / "browser-state.json"
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    page.get_by_test_id("registration-form-email-input").locator("input").fill("user.name@gmail.com")
    page.get_by_test_id("registration-form-username-input").locator("input").fill("username")
    page.get_by_test_id("registration-form-password-input").locator("input").fill("password")
    page.get_by_test_id("registration-page-registration-button").click()

    # Ждем перехода на дашборд, чтобы сессия гарантированно записалась
    expect(page).to_have_url(re.compile(r".*/dashboard"))

    context.storage_state(path=str(state_file))
    context.close()

    return str(state_file)


@pytest.fixture
def authorized_page(browser: Browser, auth_state_path: str) -> Page:
    """Создает изолированную страницу с уже загруженной сессией для каждого теста."""
    context = browser.new_context(storage_state=auth_state_path)
    page = context.new_page()
    yield page
    context.close()
