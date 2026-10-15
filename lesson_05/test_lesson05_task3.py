from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    driver.maximize_window()

    kol_vo = driver.find_elements(By.TAG_NAME, "a")
    assert len(kol_vo) == 9
    #количество тегов д.б. 9

    for i in kol_vo:
        assert i.is_displayed()
        #проверяем наличие всех ссылок на экране

    first_i = kol_vo[0]
    assert "1" in first_i.text
    #проверяем первую ссылку, д.б.'1'

    driver.quit()
