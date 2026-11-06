from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

#Вход на страницу калькулятора
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# Ввод значения таймера delay
    in_delay = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    in_delay.clear()
    in_delay.send_keys(45)

# Нажать на кнопки калькулятора
    submit_button7 = driver.find_element(By.XPATH, "// span[text() = '7']")
    submit_button7.click()
    submit_button_plus = driver.find_element(By.XPATH, "// span[text() = '+']")
    submit_button_plus.click()
    submit_button8 = driver.find_element(By.XPATH, "// span[text() = '8']")
    submit_button8.click()
    submit_button_rez = driver.find_element(By.XPATH, "//span[@class = 'btn btn-outline-warning']")
    submit_button_rez.click()

# Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    result = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    driver.quit()
