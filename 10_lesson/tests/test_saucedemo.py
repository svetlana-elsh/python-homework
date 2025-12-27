import allure
import pytest
from pages.login_page import LoginPage


@pytest.mark.saucedemo
@allure.epic("Saucedemo E-commerce")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Полный процесс оформления заказа")
@allure.description("""
Этот тест проверяет весь процесс покупки в интернет-магазине Saucedemo:
1. Авторизация стандартного пользователя
2. Добавление трех товаров в корзину
3. Переход в корзину и проверка количества
4. Оформление заказа с заполнением данных
5. Проверка итоговой суммы заказа

Ожидаемый результат: Итоговая сумма равна $58.29
""")
@allure.tag("e2e", "checkout", "critical")
def test_saucedemo_checkout_total(driver):
    """Полный E2E тест процесса оформления заказа."""

    with allure.step("Шаг 1: Открыть сайт и авторизоваться"):
        login_page = LoginPage(driver)
        products_page = login_page.open().login(
            'standard_user', 'secret_sauce'
        )
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Авторизация успешна",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Шаг 2: Добавить товары в корзину"):
        with allure.step("Добавить Sauce Labs Backpack"):
            products_page.add_to_cart('Sauce Labs Backpack')
        with allure.step("Добавить Sauce Labs Bolt T-Shirt"):
            products_page.add_to_cart('Sauce Labs Bolt T-Shirt')
        with allure.step("Добавить Sauce Labs Onesie"):
            products_page.add_to_cart('Sauce Labs Onesie')

    with allure.step("Шаг 3: Перейти в корзину"):
        cart_page = products_page.go_to_cart()

    with allure.step("Шаг 4: Проверить количество товаров"):
        items_count = cart_page.get_cart_items_count()
        with allure.step(
            f"Проверить, что в корзине 3 товара (найдено: {items_count})"
        ):
            assert items_count == 3, (
                f'В корзине должно быть 3 товара, а найдено {items_count}'
            )

        with allure.step("Перейти к оформлению заказа"):
            checkout_page = cart_page.proceed_to_checkout()

    with allure.step("Шаг 5: Заполнить информацию для доставки"):
        checkout_page.fill_checkout_info('Иван', 'Петров', '123456')

    with allure.step("Шаг 6: Проверить итоговую сумму"):
        total_amount = checkout_page.get_total_amount()
        with allure.step(f"Проверить сумму: ${total_amount}"):
            assert total_amount == '58.29', (
                f'Ожидалась сумма $58.29, но получена ${total_amount}'
            )

    allure.attach(
        f'Тест успешно пройден!\n'
        f'Итоговая сумма: ${total_amount}\n'
        f'Товаров в заказе: {items_count}',
        name='Итоги теста',
        attachment_type=allure.attachment_type.TEXT
    )

    allure.attach(
        driver.get_screenshot_as_png(),
        name="Финальный экран с суммой",
        attachment_type=allure.attachment_type.PNG
    )
