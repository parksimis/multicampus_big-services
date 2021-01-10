# 가위 바위 보 게임을 컴퓨터와 YOU로 변경

import random

shape = ['가위', '바위', '보']

player = input('YOU 입력 : ')

n = random.randint(1, 3)
computer = shape[n-1]

if (player == '가위' and computer == '보'):
    print('player win!')
elif (player == '바위' and computer == '가위'):
    print('player win!')
elif (player == '보' and computer == '바위'):
    print('player win!')
elif player == computer:
    print('비겼습니다.')
else:
    print('Computer Win')

print('컴퓨터는 ' + computer + ' 입니다.')