import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)
#проверяем значение атрибута checked у people_radio
img_element = browser.find_element_by_id("treasure")

x = img_element.get_attribute("valuex")

ans = calc(int(x))
browser.find_element_by_id("answer").send_keys(ans)
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()

browser.find_element_by_class_name("btn.btn-default").click()




