
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(12)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
if button:
    browser.find_element_by_id("book").click()
x = browser.find_element_by_id("input_value").text
browser.find_element_by_id("answer").send_keys(calc(x))
browser.find_element_by_id("solve").click()
assert "successful" in message.text

