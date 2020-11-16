# 지난 시간 했던 내용
# urllib.request 모듈을 사용(urlretrieve, urlopen)
# url을 기반으로 파일들을 수정

# 이번 시간(7교시)
# requests 모듈을 사용해 보기
# request 모듈을 직접 생성해 보기(GET, POST, ...)
# urllib.request와는 전혀 다른 라이브러리로 이름만 비수할 뿐...

import requests
#from requests import *

#url = 'https://news.google.com'
#ret = get((url))
#ret = requests.get(url)

data = {
    'localchange': '',
    'dynamicKey': '',
    'encpw': '',
    'enctp': '1',
    'svctype': '1',
    'smart_LEVEL': '1',
    'bvsd': '',
    'encnm': '',
    'locale': 'ko_kr',
    'url': 'https://www.naver.com',
    'id': 'zsw97',
    'pw': '*********' #접속하실 때는 직접 비밀번호를 data안에 입력해주시면 됩니다.
}

response = requests.post('https://nid.naver.com/nidlogin.login', data=data)
print(response.content.decode(encoding="utf-8"))
