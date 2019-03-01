# 1.我们要在百度首页找到所有的链接，并输出链接文字。

from selenium import webdriver
import time

driver=webdriver.Chrome(".\chromedriver")
try:
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    driver.switch_to.window(driver.current_window_handle)
    ele=driver.find_elements_by_tag_name("a")
    for i in ele:
        print(i.text)
    time.sleep(3)
finally:
    driver.quit()
