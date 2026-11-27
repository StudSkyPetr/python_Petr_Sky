from tkinter.font import NORMAL

import allure
import pytest
from selenium import webdriver
from pages_allure.pages_shop_allure import PagesShop


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@allure.story("Тест работы калькулятора")
@allure.severity(NORMAL)
@allure.title("Интернет-магазин")
def test_shop_pages(driver):
    url_shop = "https://www.saucedemo.com/"
    pages_shop = PagesShop(driver, url_shop)
    pages_shop.open_page_shop()
    pages_shop.authorize_in_shop("standard_user", "secret_sauce")
    pages_shop.add_product_basket()
    pages_shop.basket_shop()
    pages_shop.basket_authorization_string_shop("Петр", "Прохоров", "629603")
    pages_shop.result_total()
    assert pages_shop.result_total() == "Total: $58.29", f"Ожидалось  'Total: $58.29'"
