from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

try:
    # Ждем загрузки третьей картинки (она появляется последней)
    wait = WebDriverWait(driver, 15)
    third_img = wait.until(
        EC.presence_of_element_located((By.ID, "award"))
    )

    # Получаем атрибут src
    src_value = third_img.get_attribute("src")
    print(src_value)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
