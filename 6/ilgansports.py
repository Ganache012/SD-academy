import requests
import lxml.html

response = requests.get('http://isplus.live.joins.com/news/list/list.asp')

html = lxml.html.fromstring(response.content)

isPlusUrls = []

#xpath를 사용한 문서 구조 가져오기(스크래핑)
#크롤링(Crawlling vs Scraping) 

#elements = html.xpath('//*[@id="news_list"]/div[2]/ul/li[1]/dl/dt/a')
# //: 최상위 디렉터리
elements = html.xpath('//a[@class="title_cr"]') # 최상위 디렉토리 밑에 title_cr이라는 클래스를 가지고 있다는 뜻

for element in elements:
    print('title', element.text)
    print('url: ', element.get('href'))