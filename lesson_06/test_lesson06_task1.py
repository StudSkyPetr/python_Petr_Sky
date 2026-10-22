from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    first_url = "https://the-internet.herokuapp.com/dynamic_loading/2"
    driver.maximize_window()
    driver.get(first_url)

    # 2. Найдите и нажмите на кнопку "Start"
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    # 3. Дождитесь появления текста "Hello World!"
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"#finish")), "Hello World!")

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("screenshot_Petr/text06_1.png")
    # 5. Проверьте, что появившийся текст равен "Hello World!"
    text_1 = "Hello World!"
    text_result = driver.find_element(By.CSS_SELECTOR, "#finish")

    assert text_1 == text_result.text

    driver.quit()
