# 1. Python에서 DBMS관련 라이브러리 사용

- mysql, DBMS 사용
    - 1. facebook, instagram, news등의 댓글을 수집해서 저장(텍스트 데이터를 저장) - 영문
    - 2. openAPI를 이용해 데이터를 저장(json, xml 파싱 하는법)
    
## 1.1 구름 컨테이너에서 mysql server를 실행하는 방법

```
    #> mkdir -p /var/run/mysqld
    #> ls -ld /var/run/mysqld
    
    #> chown mysql:mysql /var/run/mysqld
    #> ls -ld /var/run/mysqld
    
    #> mysqld_safe & 
    <enter>
    
    #> netstat -ant //mysql 실행 확인 mysql port: 3306
    OR
    #> ps -ef | grep mysqld //process 목록 확인하기
    
    #> mysql -u root //프롬프트 바뀌는지 확인
```

## mysql 관련 명령어
```
    show databases; : 데이터베이스를 보여줘라
    create database 데이터베이스_이름; : DB 만들기
    drop database 데이터베이스_이름; : DB 삭제
    use 데이터베이스_이름; : DB 선택하기
```

# 댓글 수정

## 1. 신문사 등의 사이트를 이용해서 뉴스 목록을 수집