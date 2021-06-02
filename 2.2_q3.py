import os 
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)

browser.find_element_by_name("firstname").send_keys("Amir")
browser.find_element_by_name("lastname").send_keys("Nyssa")
browser.find_element_by_name("email").send_keys("Amir_lord@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__)) 
# получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'sample.txt') 
# добавляем к этому пути имя файла
element = browser.find_element_by_css_selector("[type='file']")
element.send_keys(file_path)
button = browser.find_element_by_css_selector("[type='submit']")
button.click()
