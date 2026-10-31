from playwright.sync_api import sync_playwright, expect, Page


class ProductCardComponent:
    """Компонент карточки конкретного товара на странице расценок"""

    def __init__(self, page, product_title: str):
        # Находим карточку на экране по её заголовку (например, 'VAG 06Q103485D')
        self.card = page.locator(f".product-card:has-text('{product_title}')")

        # Локаторы внутри этой карточки
        self.buy_button = self.card.locator("button:has-text('Добавить в корзину')")
        self.plus_button = self.card.locator("button.quantity-plus")  # кнопка "+"

    def increase_quantity(self):
        """Нажатие на плюс для увеличения количества товара."""
        self.plus_button.click()

    def click_buy(self):
        """Нажатие на кнопку добавления в корзину."""
        self.buy_button.click()
