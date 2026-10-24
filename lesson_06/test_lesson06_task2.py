from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    mail_url = "https://gitflic.ru/"
    driver.maximize_window()
    driver.get(mail_url)
    driver.delete_all_cookies()
    driver.refresh()

# для пользователя petr_user1
    driver.delete_all_cookies()
    driver.add_cookie({
        'name': 'SESSION',
        'value': 'NDFmYzE1YWYtZDA0ZS00NTE5LThmNjYtZWIzNWFmNWIyMzc2',
        'domain': 'gitflic.ru'
    })
    driver.refresh()
#Переходим в профиль 1 пользователя
    driver.add_cookie({
        'name': 'cookiesAccepted',
        'value': 'true',
        'domain': 'gitflic.ru'
    })
    driver.get("https://gitflic.ru/user/petr_user1")
# сохранение url_petr1
    url_petr1 = driver.current_url
    print("URL пользователя 1:", url_petr1)

    # для пользователя petr_user2
    driver.delete_all_cookies()
    driver.add_cookie({
        'name': 'SESSION',
        'value': 'Njc2NDk5OGQtZjAwMC00OTNmLWI5MmYtYzEwYzY5NDFmMjFj',
        'domain': 'gitflic.ru'
    })
    driver.refresh()
    # Переходим в профиль 2 пользователя
    driver.add_cookie({
        'name': 'cookiesAccepted',
        'value': 'true',
        'domain': 'gitflic.ru'
    })
    driver.get("https://gitflic.ru/user/petr_user2")
    # сохранение url_petr2
    url_petr2 = driver.current_url
    print("URL пользователя 2:", url_petr2)

#Сравнение урлов 1 и 2 юзеров. Они разные
    assert url_petr1 != url_petr2

    driver.quit()
