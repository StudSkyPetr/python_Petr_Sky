import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PagesCalculator:
    """Этот класс определяет данные для тестирования калькулятора"""

    delay_input = (By.CSS_SELECTOR, "#delay")
    button_num_submit = (By.XPATH, f"// span[text() = num]")
    button_action_submit = (By.XPATH, f"// span[text() = action]")
    button_rez_submit = (By.XPATH, "//span[@class = 'btn btn-outline-warning']")
    result_screen = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url : str):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.wait_45 = WebDriverWait(self.driver, 45)


    @allure.step("Открытие страницы с калькулятором")
    def open_pages(self):
        """Откратие страницы калькулятора"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


    @allure.step("Ввод времени задержки вывода результата на{delay_seconds} секунд")
    def setting_delay (self, delay_seconds:int):
        """Ввод времени задержки вывода результата (в секундах)"""
        self.wait.until(EC.presence_of_element_located(self.delay_input))
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(delay_seconds)


    @allure.step("Нажимаем цифровую клавишу {num}")
    def setting_button_num_submit(self, num : int):
        """Ввод цифры нажатием на кнопку калькулятора"""
        button_num_locator = (By.XPATH, f"//span[text()='{num}']")
        self.driver.find_element(*button_num_locator).click()


    @allure.step("Нажимаем функциональную клавишу {action}")
    def setting_button_action_submit(self, action : str):
        """Ввод нажатием на функциональную кнопку калькулятора"""
        button_action_locator = (By.XPATH, f"//span[text()='{action}']")
        self.driver.find_element(*button_action_locator).click()


    @allure.step("Ожидание и вывод результата на экран")
    def end_result_screen(self):
        """Вывод результата работы калькулятора через задержку"""
        result = WebDriverWait(self.driver, 45).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".screen")))
        end_result = WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        print(end_result)
        return result.text
