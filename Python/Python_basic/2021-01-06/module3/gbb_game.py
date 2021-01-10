# 15_function_gbb_game.py
import random

def gbb_game(player):
    computer = random.randint(1, 3)
    if computer - player == 1 or computer - player == -2:
        print('컴퓨터가 이겼습니다.')
    elif computer == player:
        print('비겼습니다.')
    else:
        print('당신이 이겼습니다.')

    print(f'COM : {computer}')

def input_num():
    player = int(input('YOU 입력 (1: 가위, 2:바위, 3: 보) : '))
    gbb_game(player)

