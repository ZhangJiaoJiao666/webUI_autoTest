from selenium import webdriver
import os

#Chorm
# dir=os.path.dirname(__file__)
# chormeDriver_path=dir+ "\chromedriver.exe"
# driver=webdriver.Chrome(chormeDriver_path)
# driver.get("http://www.yahoo.com")

# FireFox
dir=os.path.dirname(__file__)
firefoxDriver_path=dir+ "\geckodriver.exe"
driver=webdriver.Firefox(executable_path=firefoxDriver_path)
driver.get("http://python.org")
assert "我们" in driver.title

#IE
# dir=os.path.dirname(__file__)
# ieDriver_path=dir+"/IEDriverServer.exe"
# driver=webdriver.Ie(ieDriver_path)
# driver.get("http://python.org")
# assert "Python" in driver.title
