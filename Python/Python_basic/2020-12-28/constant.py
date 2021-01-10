# 상수 : 값이 변경되지 않는 저장공간
# 파이썬에서는 별도의 상수가 없음.
# 변수와 구분하기 위해 개발자가 임의로 상수를 선언
# 나중에 상수의 값을 변경해도 오류가 없음.

PI = 3.141592

r = 10
area = r*r*PI
print(area)

# ------------------------------
INT_RATE = 0.03

deposit = 10000
interest = deposit * INT_RATE
balance = deposit + interest

print(balance)
print(int(balance))

# 수치나 통화를 출력할 때 천단위 구분기호 사용하는 방법
print(format(int(balance), ','))