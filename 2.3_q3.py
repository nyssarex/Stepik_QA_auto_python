import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)


button = browser.find_element_by_css_selector("[type='submit']")
button.click()
time.sleep(1)
new_window = browser.window_handles[1]
current_window = browser.current_window_handle
browser.switch_to.window(new_window)

time.sleep(1)
#проверяем значение атрибута checked у people_radio
x = browser.find_element_by_id("input_value").text
ans = calc(x)
browser.find_element_by_id("answer").send_keys(ans)

button = browser.find_element_by_css_selector("[type='submit']")
button.click()




