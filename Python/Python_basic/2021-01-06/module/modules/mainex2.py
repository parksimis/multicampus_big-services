# mainex2.py

name = ''  # 전역변수


def input_name():
    global name  # 전역변수 값을 변경
    name = input('이름 입력 : ')

def get_name():
    if name == '':
        return '이름 없음'
    else:
        return name


def main():
    input_name()
    print(get_name())

# 현재 파일을 실행할 때 아래 코드가 동작을 하게되고,
# 현 파일이 import 되어져도 아래 코드가 실행된다.
main()

# 위 방법처럼 main() function을 만들어서 실행해 사용가능