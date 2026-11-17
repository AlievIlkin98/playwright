import pytest
from playwright.sync_api import Page

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)

@pytest.fixture
def dashboard_page(authorized_page: Page) -> DashboardPage:
    return DashboardPage(page=authorized_page)