import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 로그인 과정의 이해
# 웹에서는 인증 이슈가 굉장히 중요합니다.
# 크롤링 하는데 있어서는 큰 부분을 차지하지 않을수도 있겠지만

# 1. 인증 전/후의 html 코드를 분석(차이)
# 1.1 인증 실패시 html 코드를 봅시다!
authUrl = "https://www.ppomppu.co.kr/zboard/login_check.php?s_url=%2F"

# 2. 전달되는 매개변수
params = {
    's_url' : '%2f',
    'user_id' : '', #본인 아이디
    'password': '' # 본인 pw
}
# print(soupHtml.prettify())

# 3. 인증(로그인) 요청을 처리할 때의 HTTP 헤더 필드
headers = {
    'Host' : 'www.ppomppu.co.kr',
    'Referer' : 'https://www.ppomppu.co.kr/zboard/login.php',
    'User-Agent': 'Useragent().chrome'
}

#response = requests.get(authUrl)
#soupHtml = BeautifulSoup(response.text, 'html.parser')

element = soupHtml.find('div', class_="error2")

if element ==None:
    element = soupHtml.find('meta')
    if element['http-equiv'] == 'refresh':
        print('인증성공')
        redirectUrl = "http://www.ppomppu.co.kr"
        
elif '올바르지 않은 접근입니다.' in element.string:
    print('인증 실패')

headers['Cookie'] = response.headers['Set-Cookie']
response = requests.get(authUrl)
soupHtml = BeautifulSoup(response.text, 'html.parser')

nickName = soupHtml.select_one("span.user_nickname > a").string
print('{}님 로그인 환영!'.format(nickNmae))