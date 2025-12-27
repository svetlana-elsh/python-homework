import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """Page Object для страницы калькулятора."""

    def __init__(self, driver):
        """
        Инициализирует CalculatorPage.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.delay_input = (By.ID, 'delay')
        self.result_display = (By.CLASS_NAME, 'screen')
        self.buttons = {
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '=': (By.XPATH, "//span[text()='=']")
        }

    @allure.step("Открыть калькулятор по URL: {url}")
    def open(self, url: str) -> 'CalculatorPage':
        """
        Открывает страницу калькулятора.

        Args:
            url (str): URL страницы калькулятора

        Returns:
            CalculatorPage: текущий экземпляр CalculatorPage
        """
        self.driver.get(url)
        return self

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay(self, seconds: int) -> 'CalculatorPage':
        """
        Устанавливает задержку калькулятора.

        Args:
            seconds (int): задержка в секундах

        Returns:
            CalculatorPage: текущий экземпляр CalculatorPage
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

        allure.attach(
            f"Задержка установлена: {seconds} секунд",
            name="Параметр задержки",
            attachment_type=allure.attachment_type.TEXT
        )

        return self

    @allure.step("Нажать кнопку '{button_text}'")
    def click_button(self, button_text: str) -> 'CalculatorPage':
        """
        Нажимает кнопку калькулятора.

        Args:
            button_text (str): текст на кнопке

        Returns:
            CalculatorPage: текущий экземпляр CalculatorPage
        """
        button_locator = self.buttons.get(button_text)
        if button_locator:
            self.driver.find_element(*button_locator).click()
        return self

    @allure.step("Выполнить последовательность: {sequence}")
    def perform_calculation(self, sequence: str) -> 'CalculatorPage':
        """
        Выполняет последовательность операций на калькуляторе.

        Args:
            sequence (str): последовательность кнопок

        Returns:
            CalculatorPage: текущий экземпляр CalculatorPage
        """
        for char in sequence:
            self.click_button(char)
        return self

    @allure.step("Получить результат расчета (таймаут: {timeout} сек)")
    def get_result(self, timeout: int = 50) -> str:
        """
        Получает результат расчета.

        Args:
            timeout (int): время ожидания в секундах

        Returns:
            str: результат расчета
        """
        wait = WebDriverWait(self.driver, timeout)

        wait.until(
            lambda driver: driver.find_element(
                *self.result_display
            ).text.strip() not in ['', '7+8', '...']
        )

        result = self.driver.find_element(
            *self.result_display
        ).text.strip()

        allure.attach(
            f"Результат расчета: {result}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

        return result
