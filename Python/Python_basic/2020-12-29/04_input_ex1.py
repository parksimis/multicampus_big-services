# 04_input_ex1.py

# input() 연습문제
# 점수를 입력 받아서 총점과 평균 출력

x = int(input('국어 점수 입력 : '))
y = int(input('영어 점수 입력 : '))
z = int(input('수학 점수 입력 : '))
print('총점 : {} '.format(sum([x, y, z])))
print('평균 : {:.2f} '.format(sum([x, y, z]) / 3))
