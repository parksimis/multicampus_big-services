# 정의 부분
# 전역변수(함수 내에서도 사용될) 정의
a = 1 # 전역변수
b = 2 # 전역변수

def show():
    c = a + b #c는 지역변수
    print(a)
    print(b)
    print(c)


def add():
    global a
    a = a+1 # a가 전역변수
    c = a+b
    print('함수 내부에서 출력')
    print(a)
    print(b)
    print(c) #지역변수

b += 10

show()
add()
print('함수 외부에서 출력')
print(a)
print(b)