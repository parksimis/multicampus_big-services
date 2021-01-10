# mainex.py

name = ''  # 전역변수


def input_name():
    global name  # 전역변수 값을 변경
    name = input('이름 입력 : ')


def get_name():
    if name == '':
        return '이름 없음'
    else:
        return name


# 현재 파일이 단독 실행되면 아래 문장이 수행되고
# 다른 파일에 import 되면 수행되지 않음.

# if __name__ == '__main__': # main() 함수처럼 동작
#     input_name()
#     print(get_name())

# 위 방법으로 사용이 가능하고, OR

def main():
    input_name()
    print(get_name())


if __name__ == '__main__':
    main()

# 위 방법처럼 main() function을 만들어서 실행해 사용가능