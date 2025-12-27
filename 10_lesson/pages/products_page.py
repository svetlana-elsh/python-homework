import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage


class ProductsPage:
    """Page Object для страницы товаров Saucedemo."""

    def __init__(self, driver):
        """
        Инициализирует ProductsPage.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, 'shopping_cart_link')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'inventory_item')
            )
        )

    @allure.step("Добавить товар '{product_name}' в корзину")
    def add_to_cart(self, product_name: str) -> 'ProductsPage':
        """
        Добавляет товар в корзину.

        Args:
            product_name (str): название товара

        Returns:
            ProductsPage: текущий экземпляр ProductsPage
        """
        product_map = {
            'Sauce Labs Backpack': 'add-to-cart-sauce-labs-backpack',
            'Sauce Labs Bolt T-Shirt': 'add-to-cart-sauce-labs-bolt-t-shirt',
            'Sauce Labs Onesie': 'add-to-cart-sauce-labs-onesie'
        }
        if product_name in product_map:
            button_id = product_map[product_name]
            self.driver.find_element(By.ID, button_id).click()

            allure.attach(
                f"Товар '{product_name}' добавлен в корзину",
                name="Добавление товара",
                attachment_type=allure.attachment_type.TEXT
            )
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> CartPage:
        """
        Переходит в корзину.

        Returns:
            CartPage: экземпляр CartPage
        """
        self.driver.find_element(*self.cart_button).click()
        return CartPage(self.driver)
