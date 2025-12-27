import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    """Page Object для страницы оформления заказа Saucedemo."""

    def __init__(self, driver):
        """
        Инициализирует CheckoutPage.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.first_name_field = (By.ID, 'first-name')
        self.last_name_field = (By.ID, 'last-name')
        self.zip_code_field = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.total_label = (By.CLASS_NAME, 'summary_total_label')
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(*self.first_name_field)
        )

    @allure.step("Заполнить информацию для доставки: {first_name} "
                 "{last_name}, ZIP: {zip_code}")
    def fill_checkout_info(self, first_name: str, last_name: str,
                           zip_code: str) -> 'CheckoutPage':
        """
        Заполняет информацию для оформления заказа.

        Args:
            first_name (str): имя
            last_name (str): фамилия
            zip_code (str): почтовый индекс

        Returns:
            CheckoutPage: текущий экземпляр CheckoutPage
        """
        self.driver.find_element(
            *self.first_name_field
        ).send_keys(first_name)
        self.driver.find_element(
            *self.last_name_field
        ).send_keys(last_name)
        self.driver.find_element(
            *self.zip_code_field
        ).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

        allure.attach(
            f"Заполнены данные доставки:\n"
            f"Имя: {first_name}\n"
            f"Фамилия: {last_name}\n"
            f"ZIP код: {zip_code}",
            name="Данные доставки",
            attachment_type=allure.attachment_type.TEXT
        )

        return self

    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа.

        Returns:
            str: итоговая сумма (например, "58.29")
        """
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.total_label)
        )
        total_text = self.driver.find_element(*self.total_label).text
        amount = total_text.split('$')[1]

        allure.attach(
            f"Итоговая сумма заказа: ${amount}",
            name="Сумма заказа",
            attachment_type=allure.attachment_type.TEXT
        )

        return amount
