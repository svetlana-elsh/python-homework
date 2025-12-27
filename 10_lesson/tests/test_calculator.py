import allure
import pytest
from pages.calculator_page import CalculatorPage


@pytest.mark.calculator
@allure.epic("Slow Calculator")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тестирование калькулятора с задержкой 45 секунд")
@allure.description("""
Тест проверяет работу калькулятора с установленной задержкой.
Сценарий:
1. Открытие страницы калькулятора
2. Установка задержки 45 секунд
3. Выполнение операции 7+8
4. Ожидание и проверка результата

Особенность: Тест использует увеличенный timeout для ожидания.
""")
@allure.tag("calculator", "slow", "async")
def test_slow_calculator(driver):
    """Тест калькулятора с большой задержкой расчета."""

    calculator = CalculatorPage(driver)

    with allure.step("Шаг 1: Открыть страницу калькулятора"):
        calculator.open(
            'https://bonigarcia.dev/selenium-webdriver-java/'
            'slow-calculator.html'
        )
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Страница калькулятора открыта",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Шаг 2: Установить задержку 45 секунд"):
        calculator.set_delay(45)
        allure.attach(
            "Установлена задержка: 45 секунд",
            name="Параметр задержки",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Шаг 3: Выполнить операцию 7+8="):
        calculator.perform_calculation('7+8=')
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Операция введена",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Шаг 4: Ожидать результат (до 60 секунд)"):
        result = calculator.get_result(timeout=60)
        allure.attach(
            f"Получен результат: {result}",
            name="Результат расчета",
            attachment_type=allure.attachment_type.TEXT
        )

        with allure.step("Проверить, что результат равен 15"):
            assert result == '15', (
                f'Ожидался результат 15, но получен "{result}"'
            )

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Финальный результат",
        attachment_type=allure.attachment_type.PNG
    )
