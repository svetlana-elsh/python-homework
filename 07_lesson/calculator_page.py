from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, 'delay')
        self.result_display = (By.CLASS_NAME, 'screen')
        self.buttons = {
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '=': (By.XPATH, "//span[text()='=']")
        }

    def open(self, url):
        self.driver.get(url)
        return self

    def set_delay(self, seconds):
        """Устанавливает задержку калькулятора"""
        delay_field = self.driver.find_element(*self.delay_input)
        # Полностью очищаем поле
        delay_field.clear()
        # Вводим новое значение
        delay_field.send_keys(str(seconds))
        # Проверяем, что значение установилось
        actual_value = delay_field.get_attribute('value')
        print(f"Установлена задержка: {actual_value} секунд")
        if actual_value != str(seconds):
            print(f"ВНИМАНИЕ: Запрошено {seconds}, но установлено {
                  actual_value}")
        return self

    def click_button(self, button_text):
        button_locator = self.buttons.get(button_text)
        if button_locator:
            button = self.driver.find_element(*button_locator)
            button.click()
        return self

    def perform_calculation(self, sequence):
        for char in sequence:
            self.click_button(char)
        return self

    def get_result(self, timeout=50):
        """Ждет результат расчета"""
        wait = WebDriverWait(self.driver, timeout)

        # Ждем, пока на экране не появится что-то кроме исходного выражения
        wait.until(
            lambda driver: driver.find_element(
                *self.result_display
            ).text.strip() not in ['', '7+8', '...']
        )

        # Получаем результат
        result_text = self.driver.find_element(
            *self.result_display
        ).text
        print(f"На экране: '{result_text}'")
        return result_text.strip()
