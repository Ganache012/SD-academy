# DBMS

## 1. 관계형 데이터 베이스

### 관계형 DBMS(RDB/Relational DB)
- SQLite
- MySQL
- MariaDB
- Oracle
- ...

### 1.2. 테이블
- 데이터를 테이블 형태로 지정
- 테이블은 데이터를 저장하는 형태를 규정하는 작업(정규화)
- 테이블은 html의 테이블 혹은 엑셀의 시트와 같은 형태

|col1|col2|col3|...||
|:---:|:---:|:---:|:---:|
:---:|
| - | - | - | - | row1 |
| - | - | - | - | row2 |
| - | - | - | - | row3 |

- column은 field, 속성 등의 이름으로 부릅니다.
- row(행), 자료를 나타내는 record가 되며, 그냥 data라고도 표현
- 스키마(schema)는 이러한 데이터를 저장하는 테이블의 구조를 나타낸다.

## 2. NoSQL
- 빅데이터 (관계형 DB를 사용하지 않는 경우)
- 객체 그대로를 모델링

### 2.3. 쿼리(Query)
- SQL(Standard Query Language)

# 2. 실습

## 1. DB(DataBase)
- 데이터를 다루는 단위
- 하나의 DBMS에서 여러 형태의 데이터를 관리
- ex) 환자에 대한 데이터와 직원에 대한 데이터를 분리해서 관리할 필요가 있을 것이다.
- 환자 DB

## 2. table(데이터의 구조)

### 2.1. 문자 타입
- char: 고정 크기, 속도가 제일 빠르다
- varchar: 최대 크기내에서 가변적
- text: 가변적인 크기
- blob: 바이너리 형태, 형태가 정의되지 않는 경우

# 3. SQL

- CRUD(CREATE, READ, UPDATE, DELETE): 컴퓨터에서 처리되는 기본적인 기능

## 1. DDL(Data Definition Language) : 데이터 정의어
- attributes
  ```
    NULL/NOTNULL
    PRIMARY KEY
    FOREIGN KEY
    UNIQUE
    AUTOINCREMENT
    INTEGER/TEXT/BLOB/REAL,...
    DEFAULT
  ```
- CREATE
  ```
    CREATE 테이블 "이름" ( column_name/
    field_name
    attributes,
    coulumn_name/
    field_name
    attribute,
    ...);

  ```
- DROP
  ```
    DROP TABLE
    table_name;
    DROP DATABASE
    db_name;
  ```
- ALTER
  ```
  ALTER TABLE table_name RENAME TO new_table_name;
  ALTER TABLE table_name RENAME COLUMN TO col_name TO new_col_name;
  ALTER TABLE table_name ADD COLUMN new_column_name attribute...
  ```

## 2. DML(Data Manipulation Language) : 데이터 조작어

### 2.1. 삽입
  ```
    INSERT INTO table_name VALUES(values, ... )
    INSERT INTO table_name (column_name, ... ) VALUES (values, ...)
  ```

### 2.2. 조회
  ```
    SELECT * FROM table_name;
    SELECT column_name FROM table_name;

    -- 조건절: where
    SELECT * FROM table_name where conditions, ... (조건절)
    SELECT column_name FROM table_name where conditions, ... (조건절)

    SELECT * FROM table_name WHERE condition AND|OR condition (여러 조건을 검색할 수 있다)

    -- 정렬: ordered by
    SELECT * FROM table_name ORDER BY column_name;(오름차순)
    SELECT * FROM table_name ORDER BY column_name ASC;(오름차순)
    SELECT * FROM table_name ORDER BY column_name DESC;(내림차순)

    -- LIKE 절: '%'는 대체문자의 역할
    SELECT * FROM table_name WHERE column_name LIKE="%"
  ```

### 2.3. 삭제
    - where 절을 사용할 수가 있다.(SELECT와 동일한 방법)
    - 특정 데이터를 삭제하려면 where절이 필수이다.
  ```
    -- 테이블 내의 모든 데이터의 삭제
    DELETE FROM table_name;

    -- 특정 조건의 데이터만 삭제
    -- 이때, 조건은 primary key, unique 설정이 되어있는 필드를 선택하는 것이 좋다.
    -- 중복되는 조건에 대해서도 삭제
    DELETE FROM table_name WHERE id = 1;
  ```

### 2.4. 수정
```
    UPDATE table_name SET column_name 
    UPDATE table_name SET column_name where column_name="attributes"
```

## 3. DCL(Data Control Language) : 데이터 제어어


# CSV(Comma Seperate Value)
- 각각의 필드(컬럼)를 콤마로 형태로 구분된 텍스트 파일
- 엑셀하고는 다름
- 엑셀은 바이너리 형태, 다만 CSV는 액셀에서 지원 가능한 형태

```
    SELECT
        hr as "시간",
        weathersit as "날씨",
        round(windspeed,2) as "풍속",
        -- sum(cnt) as "자전거 대여수" 
        FROM hour WHERE dteday='2011-01-01';
```