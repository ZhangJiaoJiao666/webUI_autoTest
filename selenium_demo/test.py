from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

driver.back()
time.sleep(3)

