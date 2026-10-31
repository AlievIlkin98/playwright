
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        self.page = page
        self.email_input = self.page.get_by_test_id('login-form-email-input').locator('input')
        self.password = self.page.get_by_test_id('login-form-password-input').locator('input')
        self.login_button = self.page.get_by_test_id('login-page-login-button').locator('button')


    def navigate(self):
        self.page.goto(self.url)
