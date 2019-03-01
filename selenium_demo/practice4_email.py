# 2.在百度页面-联系我们网页中，摘取全部邮箱，使用代码来实现上述过程
from selenium import webdriver
driver=webdriver.Chrome(".\chromedriver.exe")
try:
    driver.maximize_window()
    driver.implicitly_wait(7)
    driver.get("http://www.baidu.com")
    print("百度首页已打开",driver.title)

    aboutUs_text=driver.find_element_by_link_text("关于百度")
    aboutUs_text.click()
    print("关于百度页面打开",driver.title)

    contactUs_text=driver.find_element_by_link_text("联系我们")
    contactUs_text.click()
    print("联系我们页面已打开",driver.title)

    for handle in driver.window_handles:   #在当前所有窗口中
        driver.switch_to.window(handle)
    print("页面已打开:" + driver.title)
    mail_list=driver.find_elements_by_class_name("mail-content-text")

    for i in mail_list:
        if "@" in i.text:
            print(i.text)


finally:
    driver.quit()

