-- 데이터 검색 : SELECT 문
-- 조건 검색
-- 조건을 만족하는 데이터만 검색 (WHERE)

-- SELECT 속성_리스트
-- FROM 테이블_리스트
-- [WHERE 조건] ;

-- WHERE 키워드와 함께 비교, 논리 연산자 등을 이용한 검색 조건 제시
-- 숫자, 문자, 날짜 값 등을 비교 가능
-- 조건에서 문자나 날짜 값은 작은따옴표로 묶어서 표현


-- 제품 테이블에서 한빛제과가 제조한 제품의 제품명, 재고량 단가를 확인
SELECT 제품명, 재고량, 단가
FROM 제품
WHERE 제조업체 = '한빛제과'; 

-- FROM -> WHERE -> SELECT 순으로 실행

-- AND 연산자
-- 주문 테이블에서 apple 고객이 15개 이상 주문한 주문제품, 수량, 주문일자를 확인
SELECT 주문제품, 수량, 주문일자
FROM 주문
WHERE 주문고객 = 'apple' AND 수량 >= 15;

-- OR 연산자
-- 주문 테이블에서 apple 고객이 주문했거나,  15개 이상 주문된 제품의 주문제품, 수량, 주문고객, 주문일자를 확인
SELECT 주문제품, 수량, 주문고객, 주문일자
FROM 주문
WHERE 주문고객 = 'apple' OR 수량 >= 15;


-- 제품 테이블에서 단가가 2,000원 이상이면서 3,000원 이하인 제품의
-- 제품명, 단가, 제조업체를 확인
SELECT 제품명, 단가, 제조업체
FROM 제품
WHERE 단가 BETWEEN 2000 and 3000;

SELECT 제품명, 단가, 제조업체
FROM 제품
WHERE 단가 >= 2000 and 단가 <= 3000;

-- 검색 키워드
-- LIKE : 기호 (% 나 _와 함께 사용)
-- % : 0개 이상의 문자(문자의 내용과 개수는 상관없음)
-- _ : 1개의 문자

-- LIKE '데이터%' : 데이터로 시작하는 문자열(데이터로 시작하면 길이는 상관없음)
-- EX. 김데이터(X), 데이터(O), 데이터 사무소(O)

-- LIKE '%데이터' : 데이터로 끝나는 문자열
-- EX. 데이터사무소(X), 빅데이터(O), 빅데이터 사무소(X)

-- LIKE '%데이터%' : 데이터가 포함된 문자열
-- EX. 빅데이터사무소(O), 빅데이터(O), 데이터사무소(O)

-- LIKE '데이터___' : 데이터로 시작하는 6자 길이의 문자열
-- EX. 데이터사무소(O), 강남 데이터(X)

-- LIKE '__데이터' : 데이터로 끝나는 5자 길이의 문자열
-- EX. 양재데이터(O), 빅데이터(X)

-- LIKE '__한%' : 세번째 글자가 '한'인 문자열


-- 실습
-- 1) 고객 테이블에서 성이 김씨인 고객이름, 나이, 등급, 적립금을 확인
SELECT 고객이름, 나이, 등급, 적립금
FROM 고객
WHERE 고객이름 LIKE '김%';

-- 2) 고객 테이블에서 고객 아이디가 5자인 고객의 고객 아이디, 고객이름, 등급을 검색
SELECT 고객아이디, 고객이름, 등급
FROM 고객
WHERE 고객아이디 LIKE '_____';

-- NULL 키워드
-- IS NULL : 값이 NULL인지 확인
-- IS NOT NUll : 값이 NULL이 아닌지 확인
-- 검색조건에서 NULL값은 다른 값과 크기를 비교하면 결과가 모두 거짓이 됨.

-- 고객테이블에서 나이가 아직 입력되지 않은 고객의 고객 이름을 검색
SELECT 고객이름
FROM 고객
WHERE 나이 IS NULL ;

-- 고객테이블에서 이미 나이가 입력된 고객의 고객 이름을 검색
SELECT 고객이름
FROM 고객
WHERE 나이 IS NOT NULL;


-- 정렬 검색 : ORDER BY 절
-- ORDER BY 키워드 : ORDER BY 속성1, 속성2,... [ASC|DESC]
-- SELECT
-- FROM
-- [WHERE]
-- [ORDER BY 속성_리스트] [ASC | DESC]
-- ASC Default, 오름차순
-- NULL 값 처리 : ASC 오름차순(맨 먼저 출력), DESC(내림차순)에서는 맨 마지막에 출력됨
-- FROM -> WHERE -> SELECT -> ORDER BY 순으로 실행
-- ORDER BY 절은 SQL 쿼리문의 가장 마지막에 위치해야 한다.

-- 고객 테이블에서 고객이름, 등급, 나이를 검색하되, 나이를 기준으로 내림차순 정렬
-- 내림차순 정렬 : NULL이 마지막에 표시
SELECT 고객이름, 등급, 나이
FROM 고객
ORDER BY 나이 DESC;

-- 오름차순 정렬 : NULL이 먼저 표시
SELECT 고객이름, 등급, 나이
FROM 고객
ORDER BY 3 ASC;

-- 주문 테이블에서 수량이 10개 이상인 주문의 주문고객, 주문제품, 수량, 주문일자를 검색
-- 단, 주문제품을 기준으로 오름차순 정렬하고, 동일제품을 수량을 기준으로 내림차순 정렬
SELECT 주문고객, 주문제품, 수량, 주문일자
FROM 주문
WHERE 수량 >= 10
ORDER BY 주문제품 ASC, 수량 DESC;


-- 집계 함수
-- 특정 속성값을 통계적으로 계산한 결과를 검색
-- 열 함수라고도 부름. - 개수, 합계, 평균, 최댓값, 최솟값의 계산 기능을 제공
-- NULL 속성값은 제외하고 계산
-- WHERE 절에서는 사용할 수 없고, SELECT 절이나 HAVING 절에서만 사용 가능

-- AVG()
-- 제품 테이블에서 모든 제품의 단가 평균을 검색
SELECT AVG(단가) AS 단가평균
FROM 제품;

-- 제품테이블에 접근해서 단가 필드를 추출하고 평균함수를 적용

-- SUM()
-- 한빛제과에서 제조한 제품의 재고량 합계를 제품 테이블에서 확인 - 단 추출은 재고량합계로 추출
SELECT SUM(재고량) AS '재고량합계'
FROM  제품
WHERE 제조업체 = '한빛제과';

-- COUNT()
-- 고객 테이블에 고객이 몇명 등록되어 있는지 확인
-- 7개 추출
SELECT COUNT(고객아이디) AS 고객수
FROM 고객;

-- 나이에 NULL 값이 존재하므로 6개 추출
SELECT COUNT(나이) AS 고객수
FROM 고객;

-- 전체 행 수를 반환
-- 정확한 개수를 계산하기 위해서는 보통 기본키 속성이나 *를 주로 이용
SELECT COUNT(*) AS 고객수
FROM 고객;


-- 중복을 제거한 집계함수 적용
-- DISTINCT 옵션을 통해 중복된 제조업체 제거 후 개수를 셈
-- 제품을 제조하는 거래처에 대해 몇개의 업체와 거래하고 있는지 확인
SELECT COUNT(DISTINCT 제조업체) AS '제조업체 수'
FROM 제품;


-- 논리적 오류 예제
SELECT 나이, COUNT(*) AS 고객수
FROM 고객
-- 나이 : 20, 고객수 7의 결과가 나오는데, 
-- 모든 고객의 나이가 20살이고, 7명의 고객이라는 의미를 내포하므로 논리적 오류 발생
-- 어떤 필드를 집계함수를 적용하면, 일반필드는 선택하지 말아야 한다.


-- 그룹별 검색
-- GROUP BY
-- SELECT [ALL | DISTINCT] 속성1, 집계함수(속성2)
-- FROM
-- [WHERE 조건]
-- [GROUP BY 속성리스트 [HAVING 그룹에 대한 조건]]
-- [ORDER BY [ASC | DESC]];

-- GROUP BY 키워드를 이용 : 특정 속성의 값이 같은 튜플을 모아 그룹을 만듦.
-- GROUP BY 기준 속성 HAVING 조건
-- 그룹을 나누는 기준이 되는 속성은 SELECT 절에도 작성하는 것이 좋음.

-- 주문 테이블에서 주문 제품별 수량의 합계를 확인
SELECT * FROM 주문;

SELECT 주문제품, SUM(수량)
FROM 주문
GROUP BY 주문제품 ;

-- 그룹의 기준이 되는 필드 외에 다른 필드를 SELECT 하면,
-- 그룹의 여러 필드값 중 가장 위에 있는 값이 임의 추출(논리적 오류를 일으킬 수 있다.)

SELECT 주문제품, 주문고객, SUM(수량) AS 총주문수량
FROM 주문
GROUP BY 주문제품 ;

-- GROUP BY 연산 시에는 기준 필드외에 일반 필드는 집계함수를 사용하거나 표현하지 않는다.

-- 주문제품별로 몇명의 고객이 총 몇 개를 주문했는지 확인
SELECT 주문제품, COUNT(주문고객) AS 총주문고객수, SUM(수량) AS 총주문수량
FROM 주문
GROUP BY 주문제품 ;


-- 제품 테이블에서 제조업체별로 제조한 제품의 개수와 제품 중 가장 비싼 단가를 확인
-- 제품의 개수는 제품 수라는 이름으로 출력하고, 가장 비싼 단가는 최고가라는 이름으로 출력

SELECT 제조업체, COUNT(*) AS '제품 수', MAX(단가) AS 최고가
FROM 제품
GROUP BY 제조업체 ; 


-- 제품테이블에서 제품을 3개 이상 제조한 제조업체별로 제품의 개수, 제품 중 가장 비싼 단가를 검색
SELECT 제조업체, COUNT(*) AS '제품 수', MAX(단가) AS 최고가
FROM 제품
GROUP BY 제조업체
HAVING COUNT(*) >= 3 ; 
-- GROUP 별로 적용해야 하는 조건은 HAVING 절에 기재

-- 고객 테이블에서 적립금 평균이 1,000원 이상인 등급에 대해 등급별 고객수와 적립금 평균을 확인
SELECT 등급, COUNT(*) AS '고객수', AVG(적립금) AS '평균적립금'
FROM 고객
GROUP BY 등급
HAVING AVG(적립금) >= 1000 ;


-- 주문 테이블에서 각 주문 고객이 주문한 제품의 총 주문 수량을 주문제품별로 확인
SELECT 주문고객, 주문제품, SUM(수량) AS '총주문수량'
FROM 주문
GROUP BY 주문고객, 주문제품;

