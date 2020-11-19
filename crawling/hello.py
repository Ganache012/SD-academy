# selenium  라이브러리

# 브라우저를 직접 제어할 수 있는 라이브러리
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 크롬 웹 드라이버 필요.
# https://sites.google.com/a/chromium.org/chromedriver/downloads

browser = webdriver.Chrome('C:\\Zeon\\crawling\\chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 크기 조절: 가장크게(maximize)
#browser.maximize_window()
#browser.minimize_window()
browser.set_window_size(800, 500) # 해상도(width x height)

browser.get('http://www.naver.com')

# 웹페이지 소스 출력
#print(browser.page_source)

# 웹페이지 쿠키 확인
print("COOKIES")
print(browser.get_cookies())

# 현재 URL 확인
print("URL")
print(browser.current_url)
# search = browser.find_element_by_id('query')
# CSS 셀렉터를 이용한 검색 방법
search = browser.find_element_by_css_selector('div.green_window > input#query')
search.send_keys("검색어")
# search.submit()# "검색어" 실행
search.send_keys(keys.REUTRN) # "검색어"에 대한 연관 검색어를 나타내준다.


# 브라우저 종료
#print("브라우저를 종료합니다.")
#browser.quit()