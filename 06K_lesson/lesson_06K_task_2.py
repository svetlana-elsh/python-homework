import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    # Используем WebDriver Manager для автоматической загрузки драйвера Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(browser):
    # 1. Открываем страницу калькулятора
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    wait = WebDriverWait(browser, 50)  # Таймаут больше 45 секунд

    # 2. Находим поле ввода задержки и вводим 45
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажимаем кнопки 7, +, 8, =
    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()

    # 4. Ожидаем, пока результат не станет равным 15
    # Локатор для экрана калькулятора (предположительно)
    result_screen = browser.find_element(By.CLASS_NAME, "screen")

    # Явное ожидание появления текста "15" в элементе
    # Ожидаем до 50 секунд, чтобы учесть 45-секундную задержку
    wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # 5. Проверяем результат (assert)
    result_screen = browser.find_element(By.CLASS_NAME, "screen")
    actual_result = result_screen.text
    assert actual_result == "15", (
        f"Ожидался результат 15, но получен {actual_result}"
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
