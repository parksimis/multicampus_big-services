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
