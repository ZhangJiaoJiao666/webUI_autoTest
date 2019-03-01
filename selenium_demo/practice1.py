import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dir=os.path.dirname(__file__)
ChromeDriver_path=dir+"/chromedriver.exe"
driver=webdriver.Chrome(ChromeDriver_path)
driver.get("https://wwww.yahoo.com/")
assert "Yahoo" in driver.title

enl=driver.find_element_by_name("p")
enl.send_keys('seleniumhq'+Keys.RETURN)

driver.close()



