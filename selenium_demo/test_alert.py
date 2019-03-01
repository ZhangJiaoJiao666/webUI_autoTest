from selenium import webdriver
import time

driver=webdriver.Chrome(".\chromedriver.exe")
driver.get("http://baidu.com")
driver.implicitly_wait(5)
# driver.maximize_window()

time.sleep(1)
driver.execute_script("window.alert('这是一个弹出框')")
time.sleep(2)
driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()

driver.quit()