import os
import time
from selenium import webdriver
# 打开 www.baidu.com 页面，激活当前窗口，并输出百度首页已打开；
# 通过 id 查找搜索框，键入 java 并提交搜索； 获取页面中“百度已为您找到
# 相关结果约 xxx 个”； 执行 js 脚本，显示一个框提示用户已经找到相关结
# 果

driver=webdriver.Chrome(".\chromedriver.exe")
try:
    driver.implicitly_wait(8)  # 操作等待时间 ，默认5秒
    driver.get("https://wwww.baidu.com/")  #获取百度网页
    driver.switch_to.window(driver.current_window_handle)  #激活当前窗口

    print("百度首页已打开",driver.title)  #控制台输出信息

    input_find=driver.find_element_by_id("kw")  #通过id查找搜索框
    input_find.send_keys("java")     #在搜索框中键入java

    nums=driver.find_element_by_class_name("nums")  #找"百度已为您找到....条结果"
    print("------",nums.text)   #"百度工具&为您找到相关结果约XXXX条"

    driver.switch_to.window(driver.current_window_handle) #再次激活窗口

    wait_second=20
    # driver.execute_script("window.alert(\"{},{}秒后关闭\")".format(nums.text.replace("\n","$"),wait_second))

    driver.execute_script("window.alert(\"{},{}秒后关闭\")".format(nums.text.replace("\n","$"),wait_second))
    time.sleep(wait_second)
finally:
    driver.quit()

