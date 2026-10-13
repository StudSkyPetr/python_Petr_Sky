from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib3.util import url

first_url = "https://httpbin.qa-territory.online/"
def test_navigation():
    driver = webdriver.Chrome()
    driver.get(first_url)
    driver.maximize_window()
    sleep(2)

    driver.find_element(By.CSS_SELECTOR, "[href='/forms/post']").click()

    assert "/forms/post" in driver.current_url

    sleep(2)

    driver .back()

    assert driver.current_url == first_url
    sleep(2)

    driver.quit()
