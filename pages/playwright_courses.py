from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Сначала переходим на страницу, чтобы Playwright мог работать с DOM
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # ИСПРАВЛЕНО: Объявление локаторов (последовательность и правильные test-id)
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')  # Исправлен test-id
    registration_button = page.get_by_test_id(
        'registration-page-registration-button')  # Исправлен test-id и убран .locator('button')

    # Заполнение полей
    email_input.fill('all@mail.ru')
    username_input.fill('all')
    password_input.fill('12345')

    # Нажатие на кнопку регистрации
    registration_button.click()

    page.wait_for_url('**/dashboard')

    # Сохранение состояния
    context.storage_state(path='auth.json')

    context.close()
    browser.close()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    dashboard_section = page.get_by_test_id('dashboard-drawer-list-item-button')

    expect(dashboard_section).to_be_visible()