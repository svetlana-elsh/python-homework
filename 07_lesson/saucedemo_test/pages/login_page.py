from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def open(self):
        self.driver.get('https://www.saucedemo.com/')
        return self

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(
            username
        )
        self.driver.find_element(*self.password_field).send_keys(
            password
        )
        self.driver.find_element(*self.login_button).click()
        return ProductsPage(self.driver)


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, 'shopping_cart_link')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'inventory_item')
            )
        )

    def add_to_cart(self, product_name):
        product_map = {
            'Sauce Labs Backpack': 'add-to-cart-sauce-labs-backpack',
            'Sauce Labs Bolt T-Shirt': 'add-to-cart-sauce-labs-bolt-t-shirt',
            'Sauce Labs Onesie': 'add-to-cart-sauce-labs-onesie'
        }
        if product_name in product_map:
            button_id = product_map[product_name]
            self.driver.find_element(By.ID, button_id).click()
        return self

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)
