import requests as req
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.firefox.options import Options

from fake_useragent import UserAgent
import time

#db 연동
import pymysql as db

conn = db.connect(
    host = 'localhost', # 접속할 mysql 서버의 주소
    user = 'root', # 접속할 mysql 서버의 계정(리눅스 시스템 계정 아님)
    password = '1234', # 접속할 mysql 서버의 계정 패스워드
    db =  'SDAcademy',#mysql 서버에 접속한 이후 사용할 데이터베이스
    charset = 'utf8'
)

# 브라우저의 옵션을 사용하는 방법
#options = Options()
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

response = req.get("http://corners.auction.co.kr/AllKill/AllDay.aspx")
soupDocument = bs(response.text, "html.parser")
itemlist = soupDocument.select("ul.item_list div.inner > a")

#browser = webdriver.Firefox(executable_path="./geckodriver", options=options)
browser = webdriver.Chrome(executable_path="./chromedriver", options=options)

cur = conn.cursor(db.cursors.DictCursor)
for item in itemlist:
    #browser = webdriver.Chrome(executable_path="./chromedriver", options=options)

    try:
        browser.get(item['href'])
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li#tap_moving_2')))

        review = browser.find_element_by_css_selector('li#tap_moving_2 a')
        review.click()
    except Exception as e:
        print(e)
        browser.quit()

    soupHTML = bs(browser.page_source, "html.parser")
    commentList = soupHTML.select("ul.list__review li.list-item div.box__review-text > p")
    
    # 댓글을 가져와서 db에 저장할거임
    for comment in commentList:
        query = "INSERT INTO comments(date, site_name, comment) VALUES({}, \"{}\", \"{}\")"
        tmp = db.escape_string(comment.get_text().strip())
        query = query.format('current_date()','auction', tmp)
        print('run query:', query)
        cur.execute(query)
        #print(comment.get_text())
       
    conn.commit()
    browser.quit()
    time.sleep(300)
    
#with open('./download/shop_by_html_source.html', 'w') as file: → 이 기능은 잠시 꺼둠.
#    file.write(soupHTML.prettify()) → 이 기능은 잠시 꺼둠.

browser.quit()
