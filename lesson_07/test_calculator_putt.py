import pytest
from selenium import webdriver
from pages.pages_calculator import PagesCalculator

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator(driver):
    url_calc = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    pages_calculator = PagesCalculator(driver, url_calc)
    pages_calculator.open_pages()
    pages_calculator.setting_delay(45)
    pages_calculator.setting_button_num_submit(7)
    pages_calculator.setting_button_action_submit("+")
    pages_calculator.setting_button_num_submit (8)
    pages_calculator.setting_button_action_submit("=")

    assert pages_calculator.end_result_screen() == "15", "Результат не равен сумме 7 и 8"
