# 중앙일보의 기사 목록

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup

import requests
import time

# 크롬 웹드라이버를 이용한 브라우저 객체를 생성

browser = webdriver.Chrome('C:\\Zeon\\crawling\\chromedriver.exe')
browser.set_window_size(800, 400)

# 중앙일보의 메인 페이지로 이동
browser.get('https://joongang.joins.com/')

'''
# 메인 페이지에서 기사 목록을 가져와 보기
src = browser.page_source
soupDocument = BeautifulSoup(src) # BeautifulSoup 으로 객체 변환
'''

# 메인 페이지의 소스 가져오기
src = browser.page_source
soupDocument = BeautifulSoup(src, 'html.parser')

# 메인 페이지의 기사 목록을 가져오기
# select: 전체 목록을 가져온다.
print('전체 가져오기(왼)')
elements = soupDocument.select('div.type1 ul.list_vertical a')
for gisa in elements:
    print('title: {}'.format(gisa.get_text()))
    print('link: {}'.format(gisa['href']))

print('전체 가져오기(오)')
elements_R = soupDocument.select('div.type2 ul.list_vertical a')
for gisa_R in elements_R:
    print('title: {}'.format(gisa_R.get_text()))
    print('link: {}'.format(gisa_R['href']))

# 또다른 방법: (selenium안에 css selector이용)메인 페이지의 기사 목록을 가져오기
print("(selenium의)css-selector을 이용(왼)")
element = browser.find_element_by_css_selector('div.type1 ul.list_vertical a')
element.click() # (왼)에 해당되는 맨 위의 기사가 실행된다.

# 댓글 가져오기
print("댓글을 가져옵니다.")
#comment_area = browser.find_element_by_class_name('comment_area')
#print(comment_area.text)

comment = browser.find_element_by_css_selector('p.content')
comment.text

