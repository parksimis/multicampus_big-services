# 05_input_ex2.py

# 다음과 같이 무게와 키 값을 입력받아서 BMI 지수를 계산하는 프로그램 작성
# BMI = 몸무게 / 키의 제곱

x = float(input('몸무게(킬로그램) : '))
y = float(input('키(미터): '))
print('당신의 BMI : {:.2f}'.format((x/y**2)))
