from selenium import webdriver
import os

try:
    dir = os.path.dirname(__file__)
    Chromedriver_path = dir + "/chromedriver.exe"
    driver = webdriver.Chrome(Chromedriver_path)
    driver.maximize_window()

    driver.implicitly_wait(10)
    driver.get("https://www.qiushibaike.com/text/")
    print("页面已打开", driver.title)

    while True:
        author_list = driver.find_elements_by_css_selector("h2")
        content_list = driver.find_elements_by_css_selector(".col1 .content ")
        nice_list = driver.find_elements_by_css_selector(".stats-vote>i")
        for i in range(0, len(author_list)):
            print("作者：", author_list[i].text, "\n内容：", content_list[i].text, "\n点赞数：", nice_list[i].text)
            print()
        next_page=driver.find_element_by_link_text("下一页")
        next_page.click()
        driver.switch_to.window(driver.current_window_handle)


finally:
    driver.quit()

