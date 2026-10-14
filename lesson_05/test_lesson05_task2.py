from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


second_url = ("https://httpbin.qa-territory.online/forms/post")
def test_form_submission():
    driver = webdriver.Chrome()
    driver.get(second_url)
    driver.maximize_window()
# Ваш код здесь
    driver.find_element(By.NAME, "custname").send_keys("Petr")

    sub_button = driver.find_element(
        By.XPATH, "//button[contains(text(),'Submit')]")
    sub_button.click()

    sub_url = driver.current_url
    assert sub_url != second_url
    #URL результирующий отличается от начального

    driver.quit()
