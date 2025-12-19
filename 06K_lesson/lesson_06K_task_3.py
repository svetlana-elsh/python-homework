import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def browser():
    """Фикстура для инициализации и завершения работы браузера Firefox."""
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shopping_cart_total(browser):
    # 1. Открываем сайт магазина
    browser.get("https://www.saucedemo.com/")
    wait = WebDriverWait(browser, 10)

    # 2. Авторизация пользователя standard_user
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    # Пароль для демо-сайта взят из публичных сведений[citation:4][citation:7]
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # 3. Добавляем три товара в корзину
    # Используются data-test атрибуты, характ-е для этого сайта[citation:7]
    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for item_id in items_to_add:
        browser.find_element(
            By.CSS_SELECTOR, f'button[data-test="{item_id}"]').click(
            )

    # 4. Переходим в корзину
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Нажимаем Checkout
    browser.find_element(By.ID, "checkout").click()

    # 6. Заполняем форму данными
    browser.find_element(By.ID, "first-name").send_keys("Светлана")
    browser.find_element(By.ID, "last-name").send_keys("Елшина")
    browser.find_element(By.ID, "postal-code").send_keys("141850")
    browser.find_element(By.ID, "continue").click()

    # 7. Читаем итоговую стоимость
    # Ждем появления элемента с итогом и достаем текст
    total_element = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text  # Пример: "Total: $58.29"

    # 8. Закрываем браузер (выполнится в фикстуре teardown)

    # 9. Проверяем, что итоговая сумма равна $58.29
    # Извлекаем числовое значение из строки
    total_amount = total_text.split("$")[1]  # Получаем "58.29"
    assert total_amount == "58.29", f"Итог {total_amount} не равно $58.29"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
