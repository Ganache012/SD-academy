# xml 라이브러리의 사용
# xml 분석용

import requests
import lxml.html

# requests 라이브러리를 통해서 대상 페이지를 불러옵시다.
# 일반 스포츠의 프로야구 기사 목록

response = requests.get('http://isplus.live.joins.com/news/list/list.asp')

#요청한 URL의 HTML 소스를 lxml이 분석 가능한 객체 형태로 변환
html = lxml.html.fromstring(response.content)

# Class 선택자를 통해 원하는 요소에 바로 접근
for anchor in html.cssselect('a.title_cr'):
    # 해당 요소의 'href' 속성값을 확인
    print(anchor.get('href'))
