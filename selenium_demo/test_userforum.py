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
    driver.get("http://127.0.0.1/forum.php")
    # driver.maximize_window()
    driver.implicitly_wait(5)

    first_window=driver.current_window_handle
    driver.switch_to.window(first_window)
    print("首页已打开",driver.title)
#用户登录
    userName=driver.find_element_by_name("username")
    userName.send_keys("rebecca")
    time.sleep(3)
    pwd=driver.find_element_by_name("password")
    pwd.send_keys("123456")
    time.sleep(3)
    login_btn=driver.find_element_by_css_selector(".fastlg_l em")
    login_btn.click()
    time.sleep(3)
# 默认发帖
    default_part=driver.find_element_by_css_selector(".bm_c h2 a")
    default_part.click()
    time.sleep(3)

    send_title=driver.find_element_by_css_selector(".bm_c .px")
    send_title.send_keys("问候")
    send_content=driver.find_element_by_css_selector(".tedt .pt")
    send_content.send_keys("难难难难难难")
    btn_send=driver.find_element_by_css_selector(".bm_c button")
    btn_send.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])


#默认回帖
    replay=driver.find_element_by_css_selector(".plc textarea")
    replay.send_keys("晚上好。。。。")
    btn_replay=driver.find_element_by_css_selector(".plc button")
    btn_replay.click()
    time.sleep(4)
#退出登录
    logout=driver.find_element_by_partial_link_text("退出")
    # logout=driver.find_element_by_xpath("//p/a[7]")
    logout.click()








finally:
    pass
    # driver.quit()