from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

try:
    # Находим и нажимаем на кнопку по id="ajaxButton"
    button = driver.find_element(By.ID, "ajaxButton")
    button.click()

    # Явное ожидание появления зеленой плашки
    wait = WebDriverWait(driver, 20)
    # Ожидаем, что элемент с нужным текстом станет видимым
    green_banner = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Data loaded with AJAX')]")
        )
    )

    # Получаем и выводим текст плашки
    banner_text = green_banner.text
    print(banner_text)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
