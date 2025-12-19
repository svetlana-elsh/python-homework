from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

try:
    # Находим поле ввода по ID и вводим текст
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.clear()
    input_field.send_keys("SkyPro")

    # Находим кнопку по ID и нажимаем на неё
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Явное ожидание, чтобы кнопка обновила свой текст
    wait = WebDriverWait(driver, 5)
    updated_button = wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "updatingButton"), "SkyPro"
        )
    )

    # Получаем и выводим текст кнопки
    button_text = button.text
    print(button_text)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
