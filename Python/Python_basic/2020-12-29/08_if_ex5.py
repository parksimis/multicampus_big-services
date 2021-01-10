# 다음과 같이 가위바위보 게임 작성
print('가위바위보 게임\n가위, 바위, 보 중에 하나를 입력해주세요.')
player_1 = input('홍길동 입력 : ')
player_2 = input('이몽룡 입력 : ')

if (player_1 == '가위') and (player_2 == '바위'):
    print('이몽룡이 이겼습니다.')
elif (player_1 == '가위') and (player_2 == '보'):
    print('홍길동이 이겼습니다.')
elif (player_1 == '바위') and (player_2 == '보'):
    print('이몽룡이 이겼습니다.')
elif (player_1 == '바위') and (player_2 == '가위'):
    print('홍길동이 이겼습니다.')
elif player_1 == '보' and player_2 == '가위':
    print('이몽룡이 이겼습니다.')
elif player_1 == '보' and player_2 == '바위':
    print('홍길동이 이겼습니다.')
elif (player_1 == player_2) and player_1 in ['가위', '바위', '보']:
    print('비겼습니다.')
else:
    print('가위, 바위, 보 중에 하나를 입력하세요.')

