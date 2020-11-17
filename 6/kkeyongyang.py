import requests
#import lxml.html
from lxml.html import fromstring, tostring

response = requests.get('http://www.khan.co.kr/')

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
#div#container .section_wrap .clt .sectionB .con .crt .hd_title.top a
# 내가 쓴거:elements = html.xpath('//*[@id="container"]/div[5]/div[1]/div[1]/div/div[2]/ul/li[1]/strong/a')
elements = html.xpath('//div[@class="sectionB"]//strong[@class="hd_title top"]/a')


for element in elements:
    title = element.text
    if title == None:
        title = element.xpath('./font')[0].text
    print('title: ', title)
    print(element.get('href'))