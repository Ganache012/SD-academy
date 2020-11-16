import requests
import lxml.html

response = requests.get('http://www.chosun.com/')

html = lxml.html.fromstring(response.content)

for elements in html.cssselect(
'div#fusion-app div div div:nth-child(1) section article \
div section div div:nth-child(1) div div:nth-child(1) \
div:nth-child(1) div a.text__link.story-card__headline'):
    print('{}{}'.format(response.url, elements.get('href')))