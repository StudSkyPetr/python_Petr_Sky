from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


first_url = "https://httpbin.qa-territory.online/"
def test_navigation():
    driver = webdriver.Chrome()
    driver.get(first_url)
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "HTML Form").click()

    assert "/forms/post" in driver.current_url

    driver.back()

    assert driver.current_url == first_url

    driver.quit()
