# 지역변수_전역변수.py

# 지역변수(local variable)
# 함수 내부에서 정의된 변수
# 함수안에서만 사용가능
# 함수 호출 시 생성하고
# 함수가 종료되면 소멸되어 더이상 사용할 수 없음

def show_1():
    a = 1 # 지역변수 (show() 안에서만 사용) - 변수 생성
    print(a)

show_1()
#print(a) # 함수 바깥이므로 사용 불가



# 전역변수(global variable)
# 함수 외부에서 정의된 변수
# 프로그램 내 모든 곳에서 사용가능
# 함수 내에서 전역변수 값을 변경하려면 global 카워드 사용


a = 1 # 함수 바깥에서 정의된 전역변수 a

def show():
    c = a + b #c는 지역변수
    print(a)
    print(b)
    print(c)


def add():
    print(a)
    print(b)

b = 2 # 함수 바깥에서 정의된 전역변수 b
show()
add()
print(a)
print(b)