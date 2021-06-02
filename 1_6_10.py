import time
from selenium import webdriver


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/registration1.html"

try:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector(
        '[placeholder="Input your first name"]').send_keys('Ivan')
    browser.find_element_by_css_selector(
        '[placeholder="Input your last name"]').send_keys('Ivanov')
    browser.find_element_by_css_selector(
        '[placeholder="Input your email"]').send_keys('meow')


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

