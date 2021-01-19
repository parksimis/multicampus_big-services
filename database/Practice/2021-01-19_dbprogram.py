# 사용할 테이블
"CREATE TABLE student(name VARCHAR(50) NOT NULL,\
           birth INT(8), \
           team VARCHAR(30),\
           phone VARCHAR(11),\
           address VARCHAR(30))engine=innoDB default charset=utf8;"

# - 함수(모듈)
import datetime
import pymysql

# 1. 공통 사용
## 1) 데이터베이스 연결 함수
def connect_db():
    u = 'root'
    p = '0000'
    db = 'test'
    connect = pymysql.connect(host='127.0.0.1', user=u, passwd=p, db=db, charset='utf8')
    return connect

## 2) SELECT 문 출력 함수
def print_result(result):
    print('\n-------------------------------------------------------------------------------------')
    title = ['이름', '출생연도', '소속', '전화번호', '거주지']
    ## 필드명 출력
    for t in title:
        print(t.center(11, ' '), end='\t')
    print('\n-------------------------------------------------------------------------------------')
    keys = ['name', 'birth', 'team', 'phone', 'address']

    ## 검색 결과 리스트의 원소들을 하나씩 출력
    for row in result:
        for k in keys:
            print(str(row[k]).center(11, ' '), end='\t\t')
        print('\n-------------------------------------------------------------------------------------')


# 2. 관리자 사용
def create_db():
    sql = ['DROP DATABASE IF EXISTS `test`;', 'CREATE DATABASE `test`;', 'SHOW DATABASES;']
    db_conn = connect_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor) # 이 매개변수를 집어넣으면 DBMS에서 반환되는 레코드를 딕셔너리 형태로 제공한다.

    for query in sql:
        cursor.execute(query)
        result = cursor.fetchall()

    for r in result:
        print(r)
    db_conn.close()

    return 1

def create_table():
    db_conn = connect_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    sql = ['USE `test`;',
           "CREATE TABLE student(name VARCHAR(50) NOT NULL,\
                      birth INT(4), \
                      team VARCHAR(30),\
                      phone VARCHAR(11),\
                      address VARCHAR(30)) engine=innoDB default charset=utf8;",
           'SHOW TABLES;']
    for query in sql:
        cursor.execute(query)
        result = cursor.fetchall()

    for r in result:
        print(r)

    db_conn.close()

    return 1

# 관리자 함수 호출
# create_db()
# create_table()

# 3. 기능 함수
## 1.1), 1.2) 기능을 담당
def select(query):
    db_conn = connect_db()
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    print_result(result)
    db_conn.close()

## 2, 3, 4 기능 담당
def dml_exec(query, values):
    try:
        db_conn = connect_db()
        cursor = db_conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query, values)
        db_conn.commit()
    except Exception as e:
        print(e)
        db_conn.rollback()
    finally:
        db_conn.close()

# 본 프로그램 기능
# while 문을 이용해서 사용자의 종료 명령 전까지 계속 명령어가 입력되도록 설계
## 잘못된 명령어인 경우 안내메시지가 출력됨.
# 1. 데이터 조회
#    1.1) 모든 데이터 조회(ALL) - 사용자 입력 없음
#    1.2) 조건에 맞는 데이터만 조회(FIND) - 사용자 입력 있음
#       1.2.1 이름
#       1.2.2 나이 검색
#       1.2.3 소속
#       1.2.4 전화번호
#       1.2.5 거주지
# 2. 데이터 입력
# 3. 데이터 삭제 - 수강생 1명 삭제(전체 삭제 일어나지 않게 해야 함) - 전화번호만 삭제 기준으로 설정
# 4. 데이터 변경
#   4.1) 이름변경
#   4.2) 생년월일 변경
#   4.3) 소속
#   4.4) 전화번호
#   4.5) 거주지
# 5. 종료

# 관리자가 사용할 db, table 생성 함수 생성

cmd = 'na' # 사용자에게 명령어 입력받기 위해 선언

while True:
    print('\n*** 사용 가능 메뉴 ***')
    print(' a : 모든 데이터 조회(all)')
    print(' f : 조건에 맞는 데이터 조회(find)')
    print(' i : 수강생 입력(insert)')
    print(' d : 수강생 삭제(delete)')
    print(' r : 정보변경(update)')
    print(' q : 프로그램 종료(quit)\n')

    cmd = input('메뉴 입력 : ')

    if cmd == 'a':
        sql = "SELECT * FROM student" # 모든 수강생 검색
        select(sql)

    elif cmd == 'f':
        print('검색할 기준 입력 : (이름/나이/소속/전화번호/거주지) ')
        col = input(' 입력 >> ')
        # 검색 처리 코드
        if col == '이름':
            user_name = input('\n검색할 수강생 이름은? : ')
            sql = "SELECT * FROM student WHERE name = '{}'".format(user_name)
            select(sql)

        elif col == '나이':
            print('\n검색할 범위의 숫자만 입력해주세요.')
            input_age1 = int(input('몇 살 이상을 검색하겠습니까? : '))
            input_age2 = int(input('몇 살 이하를 검색하겠습니까? : '))
            # 오늘 날짜에서 연도만 추출
            d = datetime.date.today() # 오늘 날짜 추출
            year1 = d.year - input_age2 + 1
            year2 = d.year - input_age1 + 1

            sql = "SELECT * FROM student WHERE birth BETWEEN {} AND {};".format(year1, year2)

            select(sql)

        elif col == '소속':
            group = input('\n검색할 수강 그룹을 입력하세요. (A/B/C) : ')
            sql = "SELECT * FROM student WHERE team = '{}';".format(group)
            select(sql)

        elif col == '전화번호':
            phone_num = input('\n검색할 전화번호를 입력하세요. (숫자 11자리) : ')
            sql = "SELECT * FROM student WHERE phone = '{}';".format(phone_num)
            select(sql)

        elif col =='거주지':
            adr = input('\n검색할 거주지를 입력하세요. : ')
            sql = "SELECT * FROM student WHERE address = '{}';".format(adr)
            select(sql)

        else:
            print('잘못된 검색 조건입니다. 처음 메뉴부터 다시 선택')

    elif cmd == 'i':
        user_name = input('수강생 이름 : ')
        user_birth = input('출생연도(yyyy) : ')
        user_team = input('소속 그룹(A/B/C) : ')
        user_phone = input('전화번호(11자리) : ')
        user_address = input('거주지 : ')
        sql = 'INSERT INTO student(name, birth, team, phone, address) VALUES (%s, %s, %s, %s, %s)' # INSERT 쿼리
        values = (user_name, user_birth, user_team, user_phone, user_address)
        dml_exec(sql, values)
        print('----- 해당 데이터 저장 완료 -----')

    elif cmd == 'd':
        print('수강생 삭제는 전화번호를 통해서만 가능합니다.')
        user_phone = input('목록에서 삭제할 전화번호(숫자 11자리) : ')
        sql = "DELETE FROM student WHERE phone = %s;"
        dml_exec(sql, user_phone)
        print('----- 해당 데이터 삭제 완료 -----')

    elif cmd == 'r':
        print('수강생 정보 수정은 전화번호를 통해서만 가능합니다.')
        user_phone = input('목록에서 수정할 전화번호(숫자 11자리) : ')
        # 사용자에게 해당 수강생 정보 출력
        sql = "SELECT * FROM student WHERE phone = '{}'".format(user_phone)
        select(sql)

        col = input('\n어떤 정보를 변경할건지 입력(이름/생년월일/소속/전화번호/거주지) : ')

        if col == '이름':
            user_name = input('\n해당 수강생의 수정할 이름을 입력 : ')
            sql = "UPDATE student SET name = %s WHERE phone = %s;"
            values = (user_name, user_phone)
            dml_exec(sql, values)
            print('\n 정보 변경이 완료되었습니다.')

        elif col == '생년월일':
            user_birth = input('\n해당 수강생의 수정할 출생년도 입력(yyyy) : ')
            sql = "UPDATE student SET birth = %s WHERE phone = %s"
            values = (user_birth, user_phone)
            dml_exec(sql, values)
            print('\n 정보 변경이 완료되었습니다.')

        elif col == '소속':
            user_team = input('\n해당 수강생의 수정할 그룹을 입력(A/B/C) : ')
            sql = "UPDATE student SET team = %s WHERE phone = %s"
            values = (user_team, user_phone)
            dml_exec(sql, values)
            print('\n 정보 변경이 완료되었습니다.')

        elif col == '전화번호':
            modify_phone = input('\n해당 수강생의 수정할 전화번호 입력(숫자 11자리) : ')
            sql = "UPDATE student SET phone = %s WHERE phone = %s"
            values = (modify_phone, user_phone)
            dml_exec(sql, values)
            print('\n 정보 변경이 완료되었습니다.')

        elif col == '거주지':
            user_address = input('\n해당 수강생의 수정할 거주지 입력 : ')
            sql = "UPDATE student SET address = %s WHERE phone = %s"
            values = (user_address, user_phone)
            dml_exec(sql, values)
            print('\n 정보 변경이 완료되었습니다.')

        else:
            print('잘못된 입력입니다. 처음 메뉴부터 다시 선택 ')

    elif cmd == 'q':
        print('프로그램을 종료합니다.')
        break
    else:
        print('잘못된 명령어가 입력되었습니다. 다시 입력해주세요.')