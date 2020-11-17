import requests
#import lxml.html
from lxml.html import fromstring, tostring

response = requests.get('http://www.naver.com')

#html = lxml.html.fromstring(response.content)
html = fromstring(response.content)

isPlusUrls = []

#xpath를 사용한 문서 구조 가져오기(스크래핑)
#크롤링(Crawlling vs Scraping) 


# xpath를 이용해서 동일한 요소에 접근
# / : css selector의 '>'와 같은 의미, 하위요소(직계)
# //: Css selector에서 ' '(공백)과 같은 의미
# @ : 속성을 지정할 때 사용
# *: wildcard는 여러 문자를 대체하기 위해 사용한다.(대체문자: ?, ., ) 정규표현식(regular expression)
"""elements = html.xpath('//*[@id="NM_NEWSSTAND_DEFAULT_THUMB"]/div[1]/div/div[@class="tile_view"]/\
div[@class="thumb_area"]/div/div/a[3]')
"""
elements = html.xpath('//div[@id="newsstand"]//div[@class="tile_view"]//a[@class="btn_popup"]')

for element in elements:
    #print(tostring(element))
    print(element.get('href'))