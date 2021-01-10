pos = neg = zero = 0

for i in range(1, 11):
    num = int(input(f'숫자{i} 입력 : '))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1

print('------------------------')
print(f'양의 개수 : {pos}')
print(f'음의 개수 : {neg}')
print(f'0의 개수 : {zero}')