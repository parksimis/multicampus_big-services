-- 테이블에 데이터를 저장/수정/삭제

-- 데이터 삽입 : INSERT
-- 기본 구문
-- INSERT INTO 테이블_이름[(속성_리스트)]
-- VALUES (속성값 리스트) ;
-- 속성 리스트가 생략되면 모든 필드에 생성했던 순서대로 value가 저장

-- 판매 데이터베이스의 고객테이블에 
-- 고객아이디 : strawberry, 고객이름 : 최유경, 나이 : 30, 등급 : vip, 직업 : 공무원, 적립금 : 100원
-- 인 새로운 고객의 정보 삽입
INSERT INTO 고객(고객아이디, 고객이름, 나이, 등급, 직업, 적립금)
VALUES ('strawberry', '최유경', 30, 'vip', '공무원', 100)
;

-- 확인
SELECT * FROM 고객 ;

-- 넣을 값이 없으면, 속성 리스트에서 제거해줘야함.
INSERT 
INTO 고객(고객아이디, 고객이름, 나이, 등급, 적립금)
VALUES ('tomato', '정은심', 36, 'gold', 100);

-- 확인
SELECT * FROM 고객;

-- 만약 속성리스트를 모두 넣는 경우 해당하는 위치에 NULL 값을 표시해줘야 한다.
INSERT 
INTO 고객(고객아이디, 고객이름, 나이, 등급, 적립금)
VALUES ('tomato', '정은심', 36, 'gold', NULL, 100);

-- 부속질의문을 이용해서 데이터 삽입
-- SELECT 문을 이용해서 다른 테이블에서 검색한 데이터를 삽입
-- INSERT
-- INTO 테이블이름 [(속성리스트)]
-- SELECT 문

-- 한빛제품 테이블에 제품테이블에서 검색한 데이터를 삽입
-- 한빛제품 테이블이 없기 때문에, 실행되지는 않는다.

/*
INSERT
INTO 한빛제품(제품명, 재고량, 단가)
SELECT 제품명, 재고량, 단가
FROM 제품
WHERE 제조업체 = '한빛제과';
*/


-- 저장된 데이터의 수정 : UPDATE
-- 기본 구문
-- UPDATE 테이블명
-- SET 속성이름1 = 값1, 속성이름2 = 값2, ....
-- [WHERE 조건];
-- !! UPDATE 시 WHERE 조건 없이 SET 명령만 실행하면, 해당필드의 모든 값이 변경됨 !!

-- 제품 테이블에서 제품번호가 p03인 제품의 재고량을 3000으로 수정
UPDATE 제품
SET 재고량=3000
WHERE 제품번호 = 'p03';

-- 확인
SELECT *
FROM 제품
WHERE 제품번호 = 'p03';


-- UPDATE 시 새로 저장되는 값에 수식을 적용할 수 있음.
-- 제품 테이블에 모든 제품의 단가를 10% 인상
-- 변경 전 확인
SELECT * FROM 제품;

-- UPDATE
UPDATE 제품
SET 단가 =  단가 * 1.1;

-- 확인
SELECT * FROM 제품;

-- 판매 데이터베이스에서 정소화 고객이 주문한 제품의 주문수량을 모두 5개로 수정
	-- 1) 부속 질의를 통해서 정소화 고객의 주문고객 아이디를 얻고, 
	-- 2) 해당 고객id(주문고객)에 대해서 수량 변경
	
-- 변경 전 확인
SELECT * FROM 주문;

-- UPDATE
UPDATE 주문
SET 수량 = 5
WHERE 주문고객 IN ( SELECT 고객아이디
							FROM 고객
							WHERE 고객이름 = '정소화')
;

-- 변경 후 확인
SELECT * FROM 주문;


-- 데이터 삭제 : DELETE 
-- 테이블에 저장된 데이터를 삭제
-- DELETE
-- FROM 테이블 이름
-- [WHERE 조건] ;
-- WHERE 조건 생략 시 테이블에 존재하는 모든 레코드를 삭제한다. (빈 테이블이 됨)

-- 주문 테이블에서 주문일자가 2019년 5월 22일 주문내역 삭제
- 변경 전 확인
SELECT * FROM 주문;

-- 삭제
DELETE
FROM 주문
WHERE 주문일자 = '2019-05-22'
;

-- 변경 후 확인
SELECT * FROM 주문;

-- 정소화 고객이 주문한 주문내역을 모두 삭제하시오.
-- 변경 전 확인
SELECT * FROM 주문;

-- 삭제
DELETE
FROM 주문
WHERE 주문고객 in (SELECT 고객아이디
						FROM 고객
						WHERE 고객이름 = '정소화')
;

-- 변경 후 확인
SELECT * FROM 주문;