import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.checkout_page import CheckoutPage


class CartPage:
    """Page Object для страницы корзины Saucedemo."""

    def __init__(self, driver):
        """
        Инициализирует CartPage.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.checkout_button = (By.ID, 'checkout')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'cart_item')
            )
        )

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self) -> int:
        """
        Получает количество товаров в корзине.

        Returns:
            int: количество товаров
        """
        items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        count = len(items)

        allure.attach(
            f"Найдено товаров в корзине: {count}",
            name="Количество товаров",
            attachment_type=allure.attachment_type.TEXT
        )

        return count

    @allure.step("Перейти к оформлению заказа")
    def proceed_to_checkout(self) -> CheckoutPage:
        """
        Переходит к оформлению заказа.

        Returns:
            CheckoutPage: экземпляр CheckoutPage
        """
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPage(self.driver)
