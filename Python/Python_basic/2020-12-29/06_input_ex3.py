# 06_input_ex3.py

# 그림과 같이 예금액과 이자율을 입력 받아서, 예금액, 이자율, 예금이자, 잔액 출력

deposit = int(input('예금액 입력 : '))
rate = float(input('이자율 입력(%) : '))
print('------------------------------------')
interest = deposit * rate/100
balance = deposit + interest
print('예금액 : {} '.format(deposit))
print('이자율 : {} %'.format(rate))
print('예금이자 : {} 원'.format(int(interest)))
print('잔액 : {} 원'.format(int(balance)))
print('------------------------------------')
interest = format(int(interest), ',')
balance = format(int(balance), ',')
print('예금액 : {} '.format(deposit))
print('이자율 : {} %'.format(rate))
print('예금이자 : {} 원'.format(interest))
print('잔액 : {} 원'.format(balance))
