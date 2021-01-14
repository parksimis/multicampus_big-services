-- 판매 데이터베이스 생성
-- CREATE DATABASE `판매`;

-- 고객 TABLE 만들기
-- 고객 아이디, 고객 이름, 나이, 등급, 직업, 적립금 속성
-- 고객 이름과 등급 속성은 값을 반드시 입력해야 함.
-- 적립금 속성은 값을 입력하지 않으면 0이 기본이 되도록 테이블 생성

CREATE TABLE 고객 (
	고객아이디 varchar(20) NOT NULL, 
	고객이름 varchar(10) NOT NULL,
	나이 int,
	등급 varchar(10) NOT NULL,
	직업 varchar(20),
	적립금 int DEFAULT 0,
	PRIMARY KEY(고객아이디)
);

-- 제품 TABLE 생성
-- 제품번호, 제품명, 재고량, 단가, 제조업체 속성으로 구성
-- 제품번호 기본키 
-- 재고량은 항상 0 이상 10,000개 이하

CREATE TABLE 제품 (
	제품번호 char(3) NOT NULL,
	제품명 varchar(20),
	재고량 int,
	단가 int, 
	제조업체 varchar(20),
	PRIMARY KEY (제품번호),
	CHECK (재고량 >= 0 AND 재고량 <= 10000)
);

-- 주문 TABLE 생성
-- 주문번호, 주문고객, 주문제품, 수량, 배송지, 주문일자 속성
-- 주문번호 속성이 PK
-- 주문고객 속성이 고객 테이블의 고객 아이디 속성을 참조하는 외래키
-- 주문제품 속성이 제품 테이블의 제품번호 속성을 참조하는 외래키

CREATE TABLE 주문(
		주문번호 char(3) NOT NULL,
		주문고객 varchar(20),
		주문제품 char(3),
		수량 int,
		배송지 varchar(30),
		주문일자 date,
		PRIMARY KEY(주문번호),
		FOREIGN KEY(주문고객) REFERENCES 고객(고객아이디),
		FOREIGN KEY(주문제품) REFERENCES 제품(제품번호)
);


-- 배송업체 테이블
-- 업체번호, 업체명, 주소, 전화번호 속성으로 구성
-- 업체번호 기본키

CREATE TABLE 배송업체(
	업체번호 char(3) NOT NULL,
	업체명 varchar(20),
	주소 varchar(100),
	전화번호 varchar(20),
	PRIMARY KEY (업체번호)
);


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