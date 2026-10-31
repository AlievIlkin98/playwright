from playwright.sync_api import sync_playwright, expect, Page

from playwright.sync_api import sync_playwright

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
        self.email_input = self.page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input = self.page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = self.page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = self.page.get_by_test_id('registration-page-registration-button')



    def navigate(self):
        """Открытие страницы регистрации."""
        self.page.goto(self.url)


    def register(self, email: str,username: str, password: str):
        """Заполнение формы и отправка."""
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

        self.registration_button.click()