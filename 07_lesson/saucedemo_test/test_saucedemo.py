import pytest
from pages.login_page import LoginPage


def test_saucedemo_checkout_total(driver):
    # 1. Открыть сайт и авторизоваться
    login_page = LoginPage(driver)
    products_page = login_page.open().login(
        'standard_user', 'secret_sauce'
    )

    # 2. Добавить товары в корзину
    products_page.add_to_cart('Sauce Labs Backpack')
    products_page.add_to_cart('Sauce Labs Bolt T-Shirt')
    products_page.add_to_cart('Sauce Labs Onesie')

    # 3. Перейти в корзину
    cart_page = products_page.go_to_cart()

    # 4. Проверить количество товаров и перейти к оформлению
    assert cart_page.get_cart_items_count() == 3, (
        'В корзине должно быть 3 товара'
    )
    checkout_page = cart_page.proceed_to_checkout()

    # 5. Заполнить форму оформления
    checkout_page.fill_checkout_info('Иван', 'Петров', '123456')

    # 6. Получить итоговую сумму и проверить
    total_amount = checkout_page.get_total_amount()
    assert total_amount == '58.29', (
        f'Ожидалась сумма $58.29, но получена ${total_amount}'
    )

    print(f'Тест пройден! Итоговая сумма: ${total_amount}')
