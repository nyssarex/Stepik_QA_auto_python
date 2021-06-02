from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("https://parimatch.kz/")
time.sleep(2)
login = browser.find_element_by_xpath('//button[@data-id="header-login"]')
login.click()
browser.find_element_by_name("phone").send_keys('0528')
time.sleep(3)
browser.find_element_by_name("phone").send_keys('89288')
time.sleep(2)
browser.find_element_by_id("password").send_keys('PMsmil')
time.sleep(1)
browser.find_element_by_id("password").send_keys('eik_97')
time.sleep(2)
button = browser.find_element_by_xpath('//button[@data-id="login-button"]')
time.sleep(1)
button.click()

