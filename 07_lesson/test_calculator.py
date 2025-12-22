import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    calculator = CalculatorPage(driver)

    calculator.open(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
    )
    print("Страница открыта")

    # Устанавливаем задержку
    calculator.set_delay(45)

    # Делаем расчет
    calculator.perform_calculation('7+8=')
    print("Выполнено: 7+8=")

    # Ждем результат
    result = calculator.get_result(timeout=60)  # Увеличили до 60 секунд
    print(f"Получен результат: '{result}'")

    assert result == '15', f'Ожидался результат 15, но получен "{result}"'
    print('✓ Тест успешно завершен!')
