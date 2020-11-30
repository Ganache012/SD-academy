import requests as req
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

# 브라우저의 옵션을 사용하는 방법
options = Options()
options.add_argument("-headless")

# driver = './chromedriver.exe'
browser = webdriver.Firefox(executable_path="C:\selenium\geckodriver.exe", options = options)
browser.get("http://www.naver.com")
print(browser.page_source)

browser.quit()
