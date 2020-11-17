import requests
import urllib.parse

key = "7580836326"

openAPI = "http://data.ex.co.kr/openapi/trafficapi/nationalTrafficVolumn"

values = {
   'key' : key,
   'type' : 'json',
   'sumDate' : '20201116',
}

params = urllib.parse.urlencode(values)
openAPI = openAPI + '?' + params

response = requests.get(openAPI)

data = response.json()
print(data['count'])
#print(data['list'])

for element in data['list']:
    print(element['trafficVolumn'])
    break