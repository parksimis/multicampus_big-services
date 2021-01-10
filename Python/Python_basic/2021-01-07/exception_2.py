# exception_2.py

# try ~ except ~ else

# 예외가 발생하면 except문 수행
# 예외가 발생하지 않은 경우 : else 문 수행

# try:
#   오류 가능성이 있는 코드
# except:
#   오류 처리문
# else:
#   오류가 없을 시 진행되는 구문

try:
    num = int(input('숫자 입력 : '))
except ValueError:
    print('숫자가 아닙니다.')
else:
    print(num)

# 오류 발생 시 아무것도 하지 않고 넘어가지
# 파일 읽어오기를 수행할 때
# 파일이 없어서 오류가 나면 그냥 pass하고
# 파일이 있으면 읽고 출력하기

try:
    f = open('exception.txt', 'r')
except FileNotFoundError:
    pass
else:
    data = f.read()
    print(data)
    f.close()
print('종료')

# 기능별로 필요시에는 문장마다 try except 처리를 해줘야 함.
# 예외처리는 프로그램 내부에서의 문제보다 외부와 연결되는 코드에서 예외처리르 해주게 된다.
# Ex. 사용자 입력, 파일 입출력, 메모리 관리 등등


# finally 문 : 예외 발생 여부에 상관없이 항상 수행되는 블록
try:
    f = open('exception.txt', 'r')
except FileNotFoundError:
    pass
else:
    data = f.read()
    print(data)
    f.close()
finally:
    print('종료')