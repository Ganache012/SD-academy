import requests
import lxml.html

response = requests.get('http://www.khan.co.kr/')

html = lxml.html.fromstring(response.content)

selector = 'div#container .section_wrap .clt .sectionB .con .crt .hd_title.top a'

elements = html.cssselect(selector) 

for element in elements:
    print(element.get('href'))
    if element.text == None:
        text = element.cssselect('font')[0].text
        print(text)
    else:
        print(element.text)
    #print(element.get('href'))
    #print(element.text)
    #print(lxml.html.tostring(element))