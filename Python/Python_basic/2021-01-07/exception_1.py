# exception_1.py

# 에러 종류와 상관없이
# 에러 발생하기만 하면 except 블록 수행


try:
    print(10/0)
    print('나이' + 23 +'살')
except:
    # 에러가 발생하기만 하면 except 블록을 수행
    print('오류 발생')

try:
    print(10/0)
except Exception: # 최상위 에러(모든 에러를 전부 포함하는 에러 집합)
    print('오류 발생 Exception')


# 특정 에러를 에외처리 하기 위해 에러 종류 명시

try:
    #print('나이' + 23 +'살') # 문자와 숫자를 연결했으므로 에러 처리 됨.
    print(10/0)
except ZeroDivisionError:
    print('ZeroDivision Error')

# ZeroDivision만 예외처리했기 때문에, 시스템 에러 발생

# 에러 종류 명시
# 숫자를 입력하지 않는 경우 valueError 발생

try :
    num = int(input('숫자 입력 : '))
except ValueError:
    print('숫자가 아닙니다.')


# 에러 종류 명시 as 에러 메시지 변수: 시스템에서 확인한 에러 메시지를 그대로 출력할 수도 있음
try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)

# 여러 개의 에러에 대해서 명시
# 에러는 첫번째 발생한 에러에 대해서만 처리하고 종료해버린다.
# except 구문을 반복해서 명시함으로써 가능

a = [1, 2, 3]
try:
    print(10/0)
    print(a[4])
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)


# 여러 개의 예외처리 : 함께 처리 가능
try:
    print(10/0)
    print(a[4])
except (ZeroDivisionError, IndexError) as e:
    print('오류가 발생했습니다.', e)

