## 라이브러리 import
import pymysql

# 각각 함수에서 연결된 공용 db를 같이 사용하도록 프로그램
## connection 객체를 반환
### dbconn : `glabal` 변수

dbconn = pymysql.connect(host='127.7.0.0', user='root', password='0000', database='funct_test', charset='utf8')

# 각 함수별로 예외 처리 진행
# SELECT 처리 함수 : commit 필요 없음.
## SELECT * FROM member를 처리해서 dbms로부터 넘어온 결과를 반환

def select(query):
    # 전역에 선언되어 있는 connection 객체 참조
    global dbconn
    # 커서 취득
    cursor = dbconn.cursor()
    # 쿼리 실행
    cursor.execute(query)
    # 실행된 결과 RETURN - cursor가 결과의 위치를 갖고 있음.
    # fetch 함수 이용해서 일부분을 리턴하거나 리스트 형태로 리턴도 가능하다.
    # 이 경우에는 용량이 많으면 느려지게 된다.(단점)
    return cursor # 커서 객체를 리턴함.


# DML 처리 함수 : INSERT, UPDATE, DELETE 처리
## execute() 사용
## commit 필요함 -> commit 처리 후에 에러가 발생하면 예외처리 후에 rollback 처리
## 사용자에게 쿼리와 쿼리에 사용될 값을 분리해 받아서 처리

def merge(query, values):
    # 전역에 선언되어 있는 connection 객체 참조
    global dbconn
    try:
        # 커서 취득
        cursor = dbconn.cursor()
        # 쿼리 실행
        # execute 함수는 내부에서 문자열 포맷팅으로 설정된 값에 실제 값을 매칭시켜줌.
        cursor.execute(query, values)
        dbconn.commit()
    except Exception as e:
        dbconn.rollback()

# DML을 대량 처리하는 함수 : INSERT, UPDATE, DELETE를 대량 처리하는 함수
## executemany() 사용
## commit 필요함 -> commit 처리 후에 에러가 발생하면 예외처리 후에 rollback 처리

def merge_all(query, values):
    # 전역에 선언되어 있는 connection 객체 참조
    global dbconn
    try:
        # 커서 취득
        cursor = dbconn.cursor()
        # 쿼리 실행
        # execute 함수는 내부에서 문자열 포맷팅으로 설정된 값에 실제 값을 매칭시켜줌.
        cursor.executemany(query, values)
        dbconn.commit()
    except Exception as e:
        print(e)
        dbconn.rollback()


# DML 이외의 쿼리를 실행하는 함수 (CREATE ALTER DROP)
## commit 필요함 -> commit 처리 후에 에러가 발생하면 예외처리 후에 rollback 처리

def ddl_exec(query):
    # connection 객체 가져오기
    global dbconn
    try:
        # 커서 취득
        cursor = dbconn.cursor()
        # 쿼리 실행
        cursor.execute(query)
        # 쿼리 커밋
        dbconn.commit()
    except Exception as e:
        print(e)
        dbconn.rollback()

### main
## db와 연결하는 코드는 예외처리를 반드시 하는게 좋다.

### - 사전 정의
### 어떤 테이블을 생성할 것인지? (테이블 생성 코드)
### 테이블 이름 : member
### 필드 :
### id varchar(20) NOT NULL PRIMARY KEY
### passswd varchar(20) NOT NULL
### name varchar(20) NOT NULL

try :
    # 1. 연습에 사용될 테이블이 미리 만들어져 있으면 삭제함
    ddl_exec('DROP TABLE member')


    # 2. 연습에 사용할 테이블 생성
    query = """CREATE TABLE member(
            id varchar(20) NOT NULL PRIMARY KEY,
            passwd varchar(20) NOT NULL,
            name varchar(20) NOT NULL);
            """

    ddl_exec(query=query)


    # 3. 테이블에 데이터를 넣기 위한 연습
    ## 사용자에게 값을 입력받아서 해당 값을 테이블에 저장

    ## 사용자에게 저장할 값 입력받기
    user_id = input('id를 입력하세요. : ')
    user_pwd = input('비밀번호 입력하세요. : ')
    user_name = input('이름을 입력하세요. : ')

    ### INSERT 구문 완성
    query = "INSERT INTO member VALUES (%s, %s, %s)"
    values = user_id, user_pwd, user_name
    merge(query, values)


    # # 4. 테이블에 여러 개의 정보 입력하기
    query = "INSERT INTO member VALUES (%s, %s, %s)"
    values = [('apple', 'apple', '홍길동'),
              ('peach', 'peach', '김철수')]

    # merge_all(query, values)

    # # 5. 입력된 데이터 확인
    query = 'SELECT * FROM member;'
    result = select(query)
    print(result) # 커서 객체가 리턴됨(단, SELECT 실행했기때문에 cursor가 반환결과를 가지고 있음)
    # 커서는 반복문에서 list 처럼 동작한다.
    for row in result:
        print(row)

    # # 6. 입력된 데이터를 수정
    ## 수정쿼리
    ## 사용자 아이디 별로 비밀번호 변경 가능하게 처리
    query = 'UPDATE member SET passwd=%s WHERE id = %s;'
    user_id = input('수정할 id를 입력하세요 : ')
    passwd = input('변경할 비밀번호를 입력하세요 : ')
    values = passwd, user_id
    merge(query, values)

    print('----- 수정 확인 -----')
    query = 'SELECT * FROM member;'
    result = select(query)
    for row in result:
        print(row)

    # # 7. 사용한 테이블을 삭제
    ddl_exec('DROP TABLE member')

except Exception as e :
    print(e)

finally :
    # connection 객체 사용 종료 후 리소스 닫기기
    dbconn.close()
