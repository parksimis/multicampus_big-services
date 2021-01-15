-- 제약 조건 확인 쿼리
SELECT * FROM information_schema.table_constraints;

-- 제약 조건의 삭제
-- ALTER TABLE 테이블명 DROP CONSTRAINT 제약조건 이름;

-- 고객테이블에서 20세 이상만 가입할 수 있는 제약 조건 삭제
ALTER TABLE 고객 DROP CONSTRAINT CHK_AGE;

-- 지워졌는지 확인
SELECT * FROM information_schema.table_constraints;

-- 테이블 삭제
-- DROP TABLE 테이블명;
-- 만약 삭제할 테이블을 참조하는 테이블이 있다면, 테이블 삭제는 수행되지 않음.
-- DROP 시에는 데이터뿐만 아니라 저장공간까지 모두 지움.
-- 관련된 외래키 제약조건을 먼저 삭제해야 함.

-- 배송업체 테이블을 삭제
DROP TABLE 배송업체;