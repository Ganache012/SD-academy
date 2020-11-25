import requests as req
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from fake_useragent import UserAgent

import time

headers = {
    'User-Agent' : UserAgent().chrome
}

response = req.get('https://joongang.joins.com/', headers=headers)
soupDocument = bs(response.text, "html.parser")

urls = soupDocument.select('div.type1 ul.list_vertical a:nth-child(1)')

chrome_driver = 'C:\h\chromedriver.exe'# 환경에 맞게 고쳐주세요
browser = webdriver.Chrome(chrome_driver)

browser.get(urls[0]['href'])
browser.get(urls[1]['href'])
browser.get(urls[2]['href'])
browser.get(urls[3]['href'])
browser.get(urls[4]['href'])

WebDriverWait(browser, 10).\
    until(EC.presence_of_element_located((By.CSS_SELECTOR, '.comment_list'
    )))
src = browser.page_source
soupComment = bs(src, "html.parser")

comments = soupComment.select('div.comment_list ul.list p.content')
for comment in comments:
    print(comment.get_text())

time.sleep(10)
