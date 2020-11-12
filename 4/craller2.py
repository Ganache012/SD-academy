import urllib.request as request
# import urllib.error as error
# from urllib.error import URLError, HTTPError
from urllib.error import *

# urlopen() 라이브러리 함수의 사용법

image = "https://tumblbug-pci.imgix.net/e8b360ddf31e07c1668a55083c477178ebb21da7/b1938ad26802bb57a8ca2f85dc67627f1fc561e0/e2abf43b3a96d55d738aa4d780815328377c638f/5bf7666a-df00-435c-9fcb-5d0b2ade8a05.jpg?ixlib=rb-1.1.0&w=1240&h=930&auto=format%2Ccompress&lossless=true&fit=crop&s=d4cb7baacfe9ab6973efc18f5129e91a"

# urllib에서 제공되는 urlretrieve()를 통해 다운로드를 해봤고
# urllib에서 제공되는 urlopen()를 사용해본다.

response = request.urlopen(image)

print('response-line: {} {}'.format(response.status, response.reason))
binaryImage = response.read() #이미지의 원본(바이너리)

# 그냥 쓰기모드('w')로 파일을 오픈하면 텍스트 형태의 파일로 저장이 된다.
with open('./download/Duckimage.jpg', 'wb') as file:
    file.write(binaryImage)
    

    
# 이건 강사님이 보여주신건데 해보고싶어서 하는거임
print('{} {} {}'.format(response.version, response.status, response.reason))
body = response.read()