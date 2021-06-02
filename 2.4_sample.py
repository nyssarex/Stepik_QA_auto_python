from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/cats.html"
try:
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element_by_id("button")
except Exception as e:
    print(e)

