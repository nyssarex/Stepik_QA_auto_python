import time
from selenium import webdriver

driver = webdriver.Chrome()
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://app.expertoption.com/?_ga=2.113830279.164118698.1620730197-1055423098.1620730197")
time.sleep(5)
driver.get(driver.current_url)
time.sleep(5)
driver.find_element_by_name("input").sendKeys("1")
submit_button = driver.find_element_by_css_selector(".deal-button--left.put")
submit_button.click()



