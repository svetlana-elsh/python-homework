from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, 'first-name')
        self.last_name_field = (By.ID, 'last-name')
        self.zip_code_field = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.total_label = (By.CLASS_NAME, 'summary_total_label')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.first_name_field)
        )

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_field).send_keys(
            first_name
        )
        self.driver.find_element(*self.last_name_field).send_keys(
            last_name
        )
        self.driver.find_element(*self.zip_code_field).send_keys(
            zip_code
        )
        self.driver.find_element(*self.continue_button).click()
        return self

    def get_total_amount(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total_label)
        )
        total_text = self.driver.find_element(
            *self.total_label
        ).text
        # Извлекаем сумму из текста "Total: $58.29"
        return total_text.split('$')[1]
