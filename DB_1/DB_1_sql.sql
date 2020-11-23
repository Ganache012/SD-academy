-- ALTER TABLE users RENAME COLUMN phone TO phone_number;--
-- ALTER TABLE users ADD COLUMN email TEXT ;
--INSERT INTO users(name, phone_number) VALUES("아무개", "010-xxxx-xxxx");
-- INSERT INTO users VALUES(10, "홍길동", "010-1111-1111");
-- INSERT INTO users (name, phone_number) VALUES("김까치", "010-2222-2222");
-- INSERT INTO users (name, phone_number) VALUES("이순신", "010-nnnn-nnnn"),("Godlike", "010-vvvv-vvvv");

--데이터의 모든 열과 행을 조회
-- SELECT * FROM users
-- SELECT name FROM users

-- SELECCT * FROM users ORDER BY name ASC;
-- SELECCT * FROM users ORDER BY name DESC;
-- SELECT * FROM users WHERE phone_number LIKE "010"
-- SELECT * FROM users WHERE name LIKE"이%"
-- SELECT * FROM users WHERE name LIKE"순%" (아무것도 안나옴)
--SELECT * FROM users WHERE name LIKE"%순%"

-- 삭제
--DELETE FROM users WHERE id = 1;

-- 수정
UPDATE users SET name="SYN" WHERE name="Godlike"
