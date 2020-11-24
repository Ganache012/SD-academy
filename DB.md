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

- 권한, 트랜잭션, ... 에 사용

# CSV(Comma Seperate Value)
- 각각의 필드(컬럼)를 콤마로 형태로 구분된 텍스트 파일
- 구분자를 |, tab, space, ;, ..로 사용 할 수 있다.
  - 실제 필드의 값에 콤마가 들어가는 경우
- 엑셀하고는 다름
- 엑셀은 바이너리 형태, 다만 CSV는 액셀에서 지원 가능한 형태
- 데이터 분석시에 가장 많이 사용되는 형태

```
    SELECT
        hr as "시간",
        weathersit as "날씨",
        round(windspeed,2) as "풍속",
        -- sum(cnt) as "자전거 대여수" 
        FROM hour WHERE dteday='2011-01-01';
```

# 뷰(View)

- 가상테이블
```
  CREATE VIEW myView
AS
SELECT 
	   substr(dteday, 1, 4) as "년도",
	   substr(dteday, 6, 2) as "월",
	   substr(dteday, 9, 2) as "일",
	   mnth as "월",
	   hr as "시간",
	   temp as "온도",
	   round(windspeed, 2) as "풍속",
	   cnt as "자전거 대여수"
	   FROM hour WHERE dteday="2011-01-01";
```

```
  SELECT * FROM myView
```

- 복잡한 쿼리를 단순화 할 수 있다.
- 보안상 적합하다.(조회를 제외한 다른 작업을 할 수 없다.)
  - DBMS마다 차이가 존재하다.(수정, 삭제가 가능할 수도 있다.)

# 인덱스(index)
- 데이터베이스에서: 검색을 빠르게 하기 위한 용도로 사용
  - trade-off가 존재하기 때문에, 항상 좋지는 않다.
  - 컬럼을 index로 지정하게 될 경우 생기는 문제점:
    - 1. 데이터의 양이 아주 많은 경우에 데이터가 추가되거나
    - 2. 데이터가 삭제되는 경우에 index도 동시에 업데이트가 이루어진다.
    - 3. 결국 시간이 더 오래걸리는 단점이 발생한다.

```
  CREATE INDEX index_name ON table_name(column_name, ...)
```

- 인덱스를 생성하든 하지않든 검색은 차이가 없다.
- 그냥 select 쿼리로 조회하면 인덱스가 있는경우 자동으로 참조한다.
- 따라서 그냥 만들어놓고 사용하면 됨.
- 유니크 속성의 칼럼인 경우 자동으로 인덱스를 생성하는 경우도 있다.

# 트리거(trigger)
- 방아쇠 같은 의미
- 어떤 쿼리가 실행된 경우 해당 쿼리에 대한 트리거를 설정
- 쿼리가 방아쇠가 되어서 연쇄적으로 설정된 다른 쿼리를 자동으로 실행한다.

```
  CREATE TRIGGER trigger_name BEFORE|AFTER QUERY OF
  column_name ON table_name
  BEGIN 
    SQL QUERY
  END;
```

# 정규 표현식(Regular Expression, regx)
- 문자열을 표현할 수 있는 패턴
- 거의 모든 시스템이 동일하게 정규식을 적용

```
  .: 임의의 한 문자
  []: 문자 그룹
  ^: 라인에서 시작 문자
  [^]: 부정의 의미를 나타냄
  $: 라인에서 끝나는 문자
  (): 문자열
  *: 반복(0번 이상)
  ?: 0또는 1화 매칭
  {}: 매칭되는 횟수 {min, max}
```