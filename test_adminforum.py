from selenium import webdriver
import time

driver=webdriver.Chrome("./chromedriver.exe")
driver.get("http://127.0.0.1/forum.php")
driver.implicitly_wait(5)
# driver.maximize_window()

driver.switch_to.window(driver.current_window_handle)

adminName = driver.find_element_by_name("username")
adminName.send_keys("admin")
time.sleep(3)
pwd = driver.find_element_by_name("password")
pwd.send_keys("zjj")
time.sleep(3)
login_btn = driver.find_element_by_css_selector(".fastlg_l em")
login_btn.click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
default_part = driver.find_element_by_css_selector(".bm_c h2 a")
default_part.click()
time.sleep(3)

check_input=driver.find_elements_by_xpath("//th/a[2]")
while True:
    for check in check_input:
        check.click()
        delete_content=driver.find_element_by_link_text("删除主题")
        delete_content.click()
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[0])
        delete_sure=driver.find_element_by_xpath("//p/button/span")
        delete_sure.click()
        time.sleep(3)




# for u in check_input:
#     u.click()
#     de=driver.find_element_by_link_text("删除")
#     de.click()
#     time.sleep(5)

