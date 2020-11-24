--SELECT * from hour;
-- SELECT * FROM hour WHERE dteday like"2011%";
-- SELECT * FROM hour WHERE dteday like"%-01-%";
-- SELECT mnth, hr, temp, cnt FROM hour WHERE dteday like"2011-01-01";
/* SELECT mnth as "월",
	   hr as "시간",
	   temp as "온도",
	   windspeed as "풍속",
	   cnt as "자전거 대여수"
	   FROM hour WHERE dteday="2011-01-01"; */
	   
/*SELECT 
	   substr(dteday, 1, 4) as "년도",
	   substr(dteday, 6, 2) as "월",
	   substr(dteday, 9, 2) as "일",
	   mnth as "월",
	   hr as "시간",
	   temp as "온도",
	   round(windspeed, 2) as "풍속",
	   cnt as "자전거 대여수"
	   FROM hour WHERE dteday="2011-01-01"; */

/*CREATE VIEW myView
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
	   FROM hour WHERE dteday="2011-01-01";*/
	   
-- SELECT * from myView;

/*CREATE TABLE myTable(
 name TEXT UNIQUE,
 age INTEGER
 );*/
 
 --INSERT INTO myTable VALUES("장동건", 30), ("원빈", 22), ("조진웅", 40);
 
-- 테이블 삭제
-- DROP TABLE myTable;

/*CREATE TABLE myTable(
 id INTEGER PRIMARY key AUTOINCREMENT,
 name TEXT UNIQUE,
 age INTEGER
 );*/
 
-- INSERT INTO myTable(name, age) VALUES("장동건", 30), ("원빈", 22), ("조진웅", 40);
-- INSERT INTO myTable(name, age) VALUES("박진영", 22);
-- DELETE FROM myTable;
-- INSERT INTO myTable(name, age) VALUES("박진영", 22);
--UPDATE sqlite_sequence SET seq = 0 where myTable id

-- myTable에 insert 발생시 trigger 지정
/*CREATE TRIGGER myTrigger INSERT on myTable
BEGIN
	INSERT INTO myLog(log) VALUES('Run INSERT query');
END;*/

-- INSERT INTO myTable(name, age) VALUES ("김까치", 19);
-- SELECT * FROM myLog;

/*where 절
 부등호 사용이 가능
 =: 같다(same)
 <>: 같지 않다(!=)
 >: 크다
 <: 작다
 >=: 크거나 같다
 <=: 작거나 같다
 */
-- season=1인 데이터만 보고싶을 때
-- SELECT * FROM hour WHERE season = 1;
-- season의 값이 1이 아닌 데이터만 보고싶을 때
-- SELECT * FROM hour WHERE season <> 1;

-- ex) 온도가 높은 날씨를 보고싶을때(0.5에서 0.6)
-- select * from hour where temp > 0.5 and temp < 0.6;
-- 또 다른 표현
-- SELECT * from hour where temp BETWEEN 0.5 and 0.6;

-- in
-- SELECT * FROM hour WHERE weekday IN (1,2,3,4,5)

/*
대체문자: %(여러문자), *(전체 컬럼명, 여러문자), _(문자 하나)
*/
-- SELECT * FROM hour WHERE dteday LIKE('2011%');
-- SELECT * FROM hour WHERE dteday GLOB "2011*";

-- 2011 or 2012로 시작하는 문자열
-- SELECT * FROM day WHERE dteday GLOB "201[12]*";

-- 결측치 확인
-- SELECT * FROM hour WHERE casual IS NULL;

-- 중복 제거
-- SELECT dteday FROM hour;
-- SELECT DISTINCT weathersit FROM hour;
-- SELECT ALL weathersit FROM hour;

-- select season, weathersit from hour;

-- top10
-- SELECT dteday, cnt FROM day ORDER BY cnt DESC LIMIT 10,20;

-- GROUP
-- SELECT season, sum(cnt) FROM hour GROUP BY season; 
-- SELECT yr, mnth, sum(cnt) FROM hour GROUP BY yr,mnth; 
-- SELECT yr, mnth, sum(cnt), avg(temp) FROM hour GROUP BY yr,mnth; 
-- SELECT mnth, holiday, sum(cnt) FROM hour GROUP BY mnth,weekday; 
-- SELECT workingday, avg(cnt) FROM hour GROUP BY workingday;
-- SELECT weathersit, sum(cnt) FROM hour GROUP BY weathersit;

-- HAVING

-- SELECT yr, mnth, sum(cnt), avg(temp) FROM hour GROUP BY yr, mnth HAVING avg(temp) > 0.5;
-- SELECT yr, mnth, sum(cnt), avg(temp) FROM hour GROUP BY yr, mnth HAVING sum(cnt) > 100000;

-- JOIN
/*
inner join
outer join
left join
right join

cross join
*/

-- INNER JOIN: 두 테이블간의 일치하는 컬럼이 존재하는 경우에만 합치는 경우
-- SELECT day.dteday, hour.hr FROM day INNER JOIN hour ON day.dteday = hour.dteday
-- SELECT day.cnt, myTable.name FROM day INNER JOIN myTable ON day.instant = myTable.id;

-- LEFT JOIN: 어떤 것을 기준으로 할 것이냐에 따라 다름.
-- SELECT day.cnt, myTable.name FROM day LEFT OUTER JOIN myTable ON day.instant = myTable.id

-- CROSS JOIN: 두 테이블을 그냥 합칠때 사용
SELECT day.instant, day.cnt, myTable.id, myTable.name FROM day CROSS JOIN myTable;
