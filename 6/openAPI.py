import requests
import urllib.parse

# 한국환경공단 대기오염정보

# 요청할 URL
# openAPI는 이러한 URL 형태로 제공된다.
endpoint = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"


serviceKey = 'xI%2B4mJiqwqra7nX6beGmESmUaucRJvtDqEZNGyyNwF4im%2BJRs9TCL0rAmhwuzW1a95TCqoaTxhXjjtNbzMgA%2FA%3D%3D'
#매개변수 셋팅 1.
#sidoName = 조회하고 싶은 도시
# ver = 조회하고자 하는 오퍼레이션 버전
# serviceKey = 발급받은 인증키
# _returnType = 응답 메시지 형태(json, xml)
# 매개변수의 순서는 상관이 없습니다.
#endpoint = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&\
#ver=1.3&_returnType=json&ServiceKey={}".format(serviceKey)
#http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty

# GET parameter(매개변수)
# 파이썬에 dict 타입을 사용하여 전달할 매개변수를 구성
values = {
    # key(변수명): values
    'sidoName' : '서울',
    'ver' : '1.3',
    '_returnType' : 'json',
    'ServiceKey' : serviceKey
}

#print('before: ',values)
param = urllib.parse.urlencode(values)
#print('After: ',param)

#print(endpoint)
endpoint = endpoint + '?' + param
print(endpoint)

response = requests.get(endpoint)
statusCode = response.status_code

if statusCode == 200:
    print(response.text)
else:
    print('Receive failed')