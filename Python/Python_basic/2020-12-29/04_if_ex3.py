# 정수를 입력 받아서 홀수인지 짝수인지 판별하여 출력

number = int(input('정수 입력 : '))

if number % 2 == 0:
    print('짝수')
else :
    print('홀수')

if number % 2 != 0:
    print('홀수')
else:
    print('짝수')