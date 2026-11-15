from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PagesCalculator:

    delay_input = (By.CSS_SELECTOR, "#delay")
    button_num_submit = (By.XPATH, f"// span[text() = num]")
    button_action_submit = (By.XPATH, f"// span[text() = action]")
    button_rez_submit = (By.XPATH, "//span[@class = 'btn btn-outline-warning']")
    result_screen = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.wait_45 = WebDriverWait(self.driver, 45)

    def open_pages(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def setting_delay (self, delay_seconds):
        self.wait.until(EC.presence_of_element_located(self.delay_input))
        self.driver.find_element(*self.delay_input).clear()
        self.driver.find_element(*self.delay_input).send_keys(delay_seconds)

    def setting_button_num_submit(self, num):
        button_num_locator = (By.XPATH, f"//span[text()='{num}']")
        self.driver.find_element(*button_num_locator).click()

    def setting_button_action_submit(self, action):
        button_action_locator = (By.XPATH, f"//span[text()='{action}']")
        self.driver.find_element(*button_action_locator).click()

    def end_result_screen(self):
        result = WebDriverWait(self.driver, 45).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".screen")))
        end_result = WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        print (end_result)
        return result.text

