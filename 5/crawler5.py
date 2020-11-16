import requests
import lxml.html    

#requests의 GET 메서드를 이용해 네이버의 메인 페이지를 가져오자.
response = requests.get('http://www.naver.com')

# 가져온 네이버의 메인 페이지의 html 소스코드를 lxml 객체 형태로 변환
html = lxml.html.fromstring(response.content)

#cssselect(css 선택자)를 이용해서 원하는 요소를 뽑아보자
for anchor in html.cssselect('.sc_newscast .tile_view a.btn_popup'):
    dataClick = anchor.get('data-clk')
    if dataClick == 'logo':
        print(anchor.get('href'))