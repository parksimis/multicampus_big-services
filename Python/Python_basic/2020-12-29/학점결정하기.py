# 학점결정하기.py
# 사용자로부터 점수를 입력받아 해당 점수의 학점을 결정해서 출력.

# 90 이상 A, 80이상 B, 70이상 C, 60 이상 D, 60 미만 F로 출력

score = float(input('점수를 입력하시오. : '))

if score >= 90:
    print("A")
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')