from selenium import webdriver
import os

try:
    dir=os.path.dirname(__file__)
    Chromedriver_path=dir+"/chromedriver.exe"
    driver=webdriver.Chrome(Chromedriver_path)

    driver.implicitly_wait(7)
    driver.get("https://www.qiushibaike.com/text/")

    print("页面已打开",driver.title)
    def first():
        author_list=driver.find_elements_by_css_selector("h2")
        content_list = driver.find_elements_by_css_selector(".col1 .content ")
        nice_list=driver.find_elements_by_css_selector(".stats-vote>i")
        for i in range(0,len(author_list)):
            print("作者：",author_list[i].text,"\n内容：",content_list[i].text,"\n点赞数：",nice_list[i].text)
            print()
    first()
    # def next():
    #     page=driver.find_elements_by_css_selector(".pagination>li")


finally:
    driver.quit()

