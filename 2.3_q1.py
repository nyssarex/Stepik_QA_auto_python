import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)

button = browser.find_element_by_css_selector("[type='submit']")
button.click()

alert = browser.switch_to.alert
alert.accept()
time.sleep(1)
#проверяем значение атрибута checked у people_radio
x = int(browser.find_element_by_id("input_value").text)
ans = calc(int(x))
browser.find_element_by_id("answer").send_keys(ans)

button = browser.find_element_by_css_selector("[type='submit']")
button.click()




