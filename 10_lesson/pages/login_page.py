import allure
from selenium.webdriver.common.by import By
from pages.products_page import ProductsPage


class LoginPage:
    """Page Object для страницы авторизации Saucedemo."""

    def __init__(self, driver):
        """
        Инициализирует LoginPage.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    @allure.step("Открыть страницу авторизации")
    def open(self) -> 'LoginPage':
        """
        Открывает страницу авторизации.

        Returns:
            LoginPage: текущий экземпляр LoginPage
        """
        self.driver.get('https://www.saucedemo.com/')
        return self

    @allure.step("Авторизоваться пользователем {username}")
    def login(self, username: str, password: str) -> ProductsPage:
        """
        Выполняет авторизацию пользователя.

        Args:
            username (str): имя пользователя
            password (str): пароль

        Returns:
            ProductsPage: экземпляр ProductsPage после авторизации
        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return ProductsPage(self.driver)
