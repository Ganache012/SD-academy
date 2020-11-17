#일간 스포츠
#requests 라이브러리를 통해서 대상 페이지를 불러온다.
#일간 스포츠의 프로야구 기사 목록

import requests
import lxml.html

response = requests.get('http://isplus.live.joins.com/news/list/list.asp')

html = lxml.html.fromstring(response.content)

isPlusUrls = []
for anchor in html.cssselect('a.title_cr'):
    isPlusUrls.append(anchor.get('href'))
    
print(isPlusUrls)