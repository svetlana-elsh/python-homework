import pytest
import allure
from selenium import webdriver


def pytest_addoption(parser):
    """
    Регистрация пользовательских опций командной строки.
    """
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Браузер для тестов: firefox или chrome"
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Фикстура для инициализации WebDriver.

    Yields:
        WebDriver: экземпляр WebDriver
    """
    browser_name = request.config.getoption("--browser")

    with allure.step(f"Инициализировать WebDriver для {browser_name}"):
        if browser_name.lower() == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        driver.implicitly_wait(10)
        driver.maximize_window()

    yield driver

    with allure.step("Завершить работу WebDriver"):
        driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Функция для создания отчетов Allure при падении тестов.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )
