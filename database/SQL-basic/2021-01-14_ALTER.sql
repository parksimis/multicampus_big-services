-- 테이블에 속성 추가
-- ALTER TABLE 테이블명 ADD 속성명 속성자료형 ;
-- 고객 테이블에 가입 날짜 속성을 추가

ALTER TABLE 고객 ADD 가입날짜 DATE ;
SELECT * FROM 고객;

-- 테이블의 모든 컬럼 목록 반환
SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = [테이블이름]

-- 테이블 속성을 삭제
-- ALTER TABLE 테이블명 DROP COLUMN 속성명 ;
ALTER TABLE 고객 DROP COLUMN 가입날짜;
SELECT * FROM 고객;

-- MYSQL 10이하 버전에서는 실행 안됨
-- 테이블에 제약조건 추가
-- ALTER TABLE 테이블명 ADD CONSTRAINT 제약조건이름 CHECK(조건) ;

-- 고객 테이블에 나이가 20세 이상인 회원만 가입되도록 제약조건을 추가
-- 제약조건 이름 CHK_AGE
ALTER TABLE 고객 ADD CONSTRAINT CHK_AGE CHECK(나이 >= 20);

-- 제약 조건 확인 쿼리
SELECT * FROM information_schema.table_constraints;