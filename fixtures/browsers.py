from playwright.sync_api import sync_playwright, Playwright
import pytest
from pages.registration_page import RegistrationPage

@pytest.fixture()
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    page.get_by_test_id('registration-form-email-input').locator('input').fill('TEST@mail.ru')
    page.get_by_test_id('registration-form-username-input').locator('input').fill('test')
    page.get_by_test_id('login-form-password-input').locator('input').fill('123345')
    page.get_by_test_id('registration-page-registration-button').click()

    context.storage_state(path='storage-state.json')
    browser.close()

@pytest.fixture()
def chromium_page_with_state(playwright: Playwright, initialize_browser_state):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=initialize_browser_state)
    yield context.new_page()
    browser.close()


