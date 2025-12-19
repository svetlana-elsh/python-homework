import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService


@pytest.fixture
def browser():
    edge_driver_path = (
        r"C:\Users\SharedUser\Desktop\GitPython\python-homework"
        r"\msedgedriver.exe"
    )
    service = EdgeService(executable_path=edge_driver_path)
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(browser):
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java"
        "/data-types.html"
    )
    wait = WebDriverWait(browser, 10)

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in form_data.items():
        field = browser.find_element(By.NAME, field_name)
        field.clear()
        if value:
            field.send_keys(value)

    submit_button = browser.find_element(
        By.CSS_SELECTOR, "button.btn-outline-primary"
    )
    submit_button.click()

    wait.until(EC.url_contains("data-types-submitted.html"))

    zip_code_element = browser.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_element.get_attribute("class")

    success_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in success_fields:
        element = browser.find_element(By.ID, field_id)
        assert "alert-success" in element.get_attribute("class")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
