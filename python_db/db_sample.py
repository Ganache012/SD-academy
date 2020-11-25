import pymysql as db

conn = db.connect(
    host = 'localhost', # 접속할 mysql 서버의 주소
    user = 'root', # 접속할 mysql 서버의 계정(리눅스 시스템 계정 아님)
    password = '1234', # 접속할 mysql 서버의 계정 패스워드
    db =  'SDAcademy',#mysql 서버에 접속한 이후 사용할 데이터베이스
    charset = 'utf8'
)

#cur = conn.cursor()
cur = conn.cursor(db.cursors.DictCursor)

#db 쿼리를 불러온다.
query = "SELECT Host, User FROM mysql.user"
numOfRows = cur.execute(query)

# 해당 테이블의 값을 출력하게 해주는 for문
rows = cur.fetchall()
for row in rows:
    print(row)