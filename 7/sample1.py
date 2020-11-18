# BeautifulSoup 라이브러리 활용법

# 실습용 HTML 파일이 필요
# 매번 다운로드 할 수 없으니 파일 형태로 저장후
# 파일을 불러와서 적용

# html 파일을 저장
# 1. urllib.request.urlretrieve(그림, html, 파일, .....)
# 2. urllib.request.urlopen
# 3. requests

import urllib.request as request
import requests
from bs4 import BeautifulSoup

'''
documentUrl = "https://ko.wikipedia.org/wiki/%EA%B8%B0%EA%B3%84_%ED%95%99%EC%8A%B5"

#리눅스인 경우
# 경로: /workspace/SDAcademy_python/7/sample.html
# 상대 경로: ./7/sample.html
documentPath = "/workspace/SDAcademy_python/7/sample.html"

# urlretrieve를 통한 html 문서 다운로드
# request.urlretrieve(document, path)
try:
    response = requests.get(documentUrl)
    # text 속성인 경우는 str 타입
    # content 속성인 경우는 bytes 타입
    # 파일로 저장할 시에 text 속성의 값이나 content.decode() 한 값을 저장하면 된다.
    # 한글 인코딩인 경우'utf-8'이거나 'euc-kr' 둘중에 하나일 거다.
    with open(documentPath, 'w') as file:
        file.write(response.text)
    print(response.content.decode(encoding = 'utf-8')) #content: html 소스들을 볼 수 있게 해준다.
except Exception as e:
    print(e)
'''

filePath = "/workspace/SDAcademy_python/7/sample.html"
# 실습용 html 문서를 불러오기
with open(filePath, 'r', encoding = 'utf-8') as file:
    document = file.read()
'''
# 불러온 html 문서에 beautifulSoup을 적용
# BeautifulSoup 객체로 변환
#print(type(document))
soupDoc = BeautifulSoup(document, 'html.parser')
#print(type(soupDoc))

# 웹에서의 beautify 기능을 제공
#print(soupDoc.prettify())

#태그 선택
element = soupDoc.html.body.div
print("div 태그 검색:",element)

# 다음 태그 선택
next_element = element.next_sibling.next_sibling
print("다음 태그: ",next_element)

# 텍스트 출력:h1 가져오기
h1 = soupDoc.html.body.h1
print(h1)
print(h1.string)

# 다음 엘리먼트 선택
#print(element.next_elements)
#print(list(element.next_elements))


#for ele in element.next_elements:
    #print(ele)
    #break
    
element = soupDoc.html.body.div

print(element)
# 모든 하위 요소를 포함한 요소들의 리스트
for i, ele in enumerate(element.next_elements):
    if i < 20:
        print(ele)
        
'''
# find, find_all 메소드 이용

# 찾고자하는 태그를 검색할때 사용
soupDoc = BeautifulSoup(document, 'html.parser')
h1 = soupDoc.find('h1')
print(h1)

div = soupDoc.find('div')
print(div)

h2 = soupDoc.find('h2')
print(h2)

h3 = soupDoc.find('h3')
print(h3)

# 특정 조건으로 검색하고 싶은 경우
# div 태그에서 id가 siteNotice 인 경우
div = soupDoc.find('div', id='siteNotice')
print(div)

# 특정 조건을 여러개 두고 싶은 경우:dictionary 속성을 이용할 수 있다.
print('특정 조건을 여러개 두고 싶은 경우 입니다.')
condition = {
    'id' : 'siteNotice',
    'class' : 'mw-body-content'
}
print('find 함수 이용')
div = soupDoc.find('div', attrs=condition)
print(div)

condition = {
    'class' : 'noprint'
}

print('find_all 함수 이용')
div = soupDoc.find_all('div', attrs=condition)
print(div)

# find vs find_all
# 조건에 맞는 태그를 전부 찾거나,
# 처음 매칭 되는 태그를 찾거나의 차이

# find_all은 결과를 리스트 형태로 돌려준다.

for element in div: 
    print(element)
    
# 검색한 태그의 value를 추출
# 자식 요소가 있는 경우와 없는 경우
print('h1 입니다.')
h1 = soupDoc.find('h1')
print(h1.get_text())
print(h1['lang']) # 속성값 추출

print('div 입니다')
div = soupDoc.find('div', id = 'content')
print(div.get_text())

# (선택자) select_one, select
# CSS 선택자를 통해 요소를 선택
# lxml과 유사한 접근 방법
# id 속성의 값을 이용한 선택
div = soupDoc.select_one('div#content')
print(div)

# 자식 요소를 선택
anchor = soupDoc.select_one('div#content > a')
print(anchor)

# 요소의 속성을 이용한 선택
h1 = soupDoc.select_one('h1[lang="ko"]')
print(h1)

div = soupDoc.select('div.noprint')
print(div)