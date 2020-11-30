import requests
import urllib.parse
import json
#db 연동
import pymysql as db

conn = db.connect(
    host = 'localhost', # 접속할 mysql 서버의 주소
    user = 'root', # 접속할 mysql 서버의 계정(리눅스 시스템 계정 아님)
    password = '1234', # 접속할 mysql 서버의 계정 패스워드
    db =  'SDAcademy',#mysql 서버에 접속한 이후 사용할 데이터베이스
    charset = 'utf8'
)

authKey = 'LCYY9XEU8MWCPCHMEBIC'

# 한국은행 환율 정보
endpoint = "http://ecos.bok.or.kr/api/StatisticSearch/LCYY9XEU8MWCPCHMEBIC/json/kr/1/2000/036Y003/DD/202001/202011/" #{}: 인증키
endpoint = endpoint.format(authKey)

response = requests.get(endpoint)
raw_data = json.loads(response.text) #json 형태로 바꿔준다.

cur = conn.cursor(db.cursors.DictCursor)
for row in raw_data['StatisticSearch']['row']:
    itemCode = int(row['ITEM_CODE1']) # 리스트를 숫자로 표현
    itemName = row['ITEM_NAME1']
    dataValue = float(row['DATA_VALUE']) #실수형
    time = row['TIME']
    
    query = "INSERT INTO fx(itemCode, itemName, dataValue, time) VALUES({},\"{}\",{},\"{}\")"
    query = query.format(itemCode, itemName, dataValue, time)
    cur.execute(query)
    conn.commit()