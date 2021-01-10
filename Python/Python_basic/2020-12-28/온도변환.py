# 변수_온도변환.py

# 화씨 온도를 섭씨 온도로 변환하는 프로그램

fTemp = 90
cTemp = (fTemp - 32) * 5 / 9

print(cTemp)
print("%f" % cTemp)

# print문 안에 format() 함수를 사용해서 소수점 이하 자릿수를 설정 가능

print(format(cTemp, '10.2f'))