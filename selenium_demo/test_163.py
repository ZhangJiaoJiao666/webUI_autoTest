from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

dir=os.path.dirname(__file__)
chromDriver_path=dir+"/chromedriver.exe"
driver=webdriver.Chrome(chromDriver_path)
try:
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://mail.163.com/")
    driver.switch_to.frame(0)
    user_name=driver.find_element_by_name("email")
    user_name.send_keys("12345")
    time.sleep(2)
    pwd=driver.find_element_by_name("password")
    pwd.send_keys("12345")
    time.sleep(3)
    btn_login=driver.find_element_by_id("dologin")
    btn_login.click()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(4)



finally:
    driver.quit()