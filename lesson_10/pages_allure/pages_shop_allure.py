import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PagesShop:

    # авторизация в магазине
    INPUT_LOGIN = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    # загрузка товаров
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TSHIRT_BTN = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE_BTN = (By.ID, "add-to-cart-sauce-labs-onesie")

    # Переход в корзину
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_container a")
    CHECKOUT_BTN = (By.CSS_SELECTOR, ".checkout_button")

    # Авторизация в корзине
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")


    def __init__(self, driver, url : str):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 15)


    @allure.step("Открытие страницы интернет магазина")
    def open_page_shop(self):
        #Открывает страницу интернет магазина
        self.driver.get(self.url)

    @allure.step("Авторизация на странице: ввод логина пароля")
    def authorize_in_shop(self, username : str, password : str):
        """Авторизация на странице (ввод логина и пароля"""
        self.wait.until(EC.visibility_of_element_located(
            self.INPUT_LOGIN)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(
            self.INPUT_PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(
            self.LOGIN_BUTTON)).click()

    @allure.step("Добавление товаров в корзину покупателя")
    def add_product_basket(self):
        """Добавление товаров в корзину покупателя"""
        self.wait.until(EC.element_to_be_clickable(
            self.ADD_BACKPACK_BTN)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.ADD_TSHIRT_BTN)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.ADD_ONESIE_BTN)).click()

    @allure.step("Переход в корзину с товарами")
    def basket_shop(self):
        """Переход в корзину покупателя"""
        self.wait.until(EC.element_to_be_clickable(
            self.CART_LINK)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.CHECKOUT_BTN)).click()

    @allure.step("Авторизация в корзине: данные покупателя")
    def basket_authorization_string_shop(self, first_name : str,
                                         last_name : str, postal_code : str):
        """Авторизация в корзине"""
        self.wait.until(EC.visibility_of_element_located(
            self.FIRST_NAME_INPUT)).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located(
            self.LAST_NAME_INPUT)).send_keys(last_name)
        self.wait.until(EC.visibility_of_element_located(
            self.POSTAL_CODE_INPUT)).send_keys(postal_code)
        self.wait.until(EC.element_to_be_clickable(
            self.CONTINUE_BTN)).click()

    @allure.step("Оценка результата покупки (Total:$58.29)")
    def result_total(self)->str:
        """Оценка стоимости покупок"""
        total_element = self.wait.until(EC.visibility_of_element_located(
            self.TOTAL_LABEL))
        return total_element.text
