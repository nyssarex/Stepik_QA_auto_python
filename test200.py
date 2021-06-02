from selenium import webdriver
import time

link = 'http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    input1.send_keys('Roman')
    input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    input2.send_keys('Kusochkov')
    input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
    input3.send_keys('Kus@mail.ru')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

finally:

    time.sleep(10)
    browser.quit()