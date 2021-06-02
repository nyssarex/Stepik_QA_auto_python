from selenium import webdriver
import time

from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)
time.sleep(1.5)
ans = int(browser.find_element_by_id("num1").text)+int(browser.find_element_by_id("num2").text)
select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(str(ans))

browser.find_element_by_class_name("btn.btn-default").click()


