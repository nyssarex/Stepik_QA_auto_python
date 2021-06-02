from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")
x = browser.find_element_by_id("input_value").text
browser.find_element_by_id("answer").send_keys(calc(int(x)))

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()


option2 = browser.find_element_by_id("robotsRule")
option2.click()

button = browser.find_element_by_css_selector("button.btn.btn-default")
button.click()
