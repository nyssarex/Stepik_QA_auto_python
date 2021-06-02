import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)
#проверяем значение атрибута checked у people_radio
x_val = int(browser.find_element_by_id("input_value").text)
   
ans = calc(int(x_val))
browser.find_element_by_id("answer").send_keys(ans)

button =  browser.find_element_by_class_name("btn.btn-primary")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
button.click()

