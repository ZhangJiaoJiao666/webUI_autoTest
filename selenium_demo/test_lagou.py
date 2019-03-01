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
    driver.get("https://www.lagou.com/quanguo-zhaopin/Javagongchengshi/?utm_source=m_cf_cpt_baidu_pc")
    # driver.maximize_window()
    driver.implicitly_wait(5)

    first_window=driver.current_window_handle
    driver.switch_to.window(first_window)
    print("首页已打开",driver.title)


    while True:
        jobs = driver.find_elements_by_css_selector(".item_con_list li")
        for job in jobs:
            job_link=job.find_element_by_css_selector(".p_top a h3")

            job_link.click()
            driver.switch_to.window(driver.window_handles[1])
            jobCommpany_list = driver.find_element_by_css_selector(".position-head .company")
            jobName_list=driver.find_element_by_css_selector(".position-head .name")
            money_list=driver.find_element_by_css_selector(".position-head .salary")
            print("公司：",jobCommpany_list.text,
                  "\n薪资：",money_list.text,
                  "\n职位：",jobName_list.text)
            print()
            driver.close()
            driver.switch_to.window(first_window)
            time.sleep(5)

        nextPage=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.item_con_pager .pager_container > * :last-child')))
        next_page_css=nextPage.get_attribute("class")
        if "pager_next_disabled" in next_page_css:
            break
        else:
            nextPage.click()
            driver.switch_to.window(first_window)
finally:
    pass
    # time.sleep(2)
    # driver.quit()
