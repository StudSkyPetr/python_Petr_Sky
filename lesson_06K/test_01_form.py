from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        wait = WebDriverWait(driver, 35)

        # Переход на страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Заполняем форму
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # Zip code оставляем пустым
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Нажимаем кнопку Submit
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()

        # Ждём появления поля ZIP Code
        zip_red = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

        # Предположим, что zip_code_element - это элемент, который ты проверяешь
#        zip_code_element = driver.find_element(By.CSS_SELECTOR, "#zip-code")

        # Получаем текущий стиль элемента
#        current_style = zip_code_element.get_attribute('style')

        # Выводим стиль в консоль
#        print("Текущий стиль поля Zip code:", current_style)

        assert "alert py-2 alert-danger" in zip_red.get_attribute("class"), "Поле Zip должно быть красным"

        # Проверяем остальные поля
        fields = {
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company"
        }

        # Проверяем каждое поле
        for subject in fields:
            green_fild = wait.until(EC.presence_of_element_located((By.ID, subject)))
            print(green_fild.get_attribute("subject"))

            green_fild_class = green_fild.get_attribute("class")
            # Проверяем введённые значения
            assert "alert py-2 alert-success" in green_fild_class, f"Поле {subject} должно быть зеленым"

    finally:

        driver.quit()
