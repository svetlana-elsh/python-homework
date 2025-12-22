from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.checkout_page import CheckoutPage


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, 'checkout')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'cart_item')
            )
        )

    def get_cart_items_count(self):
        items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        return len(items)

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPage(self.driver)
