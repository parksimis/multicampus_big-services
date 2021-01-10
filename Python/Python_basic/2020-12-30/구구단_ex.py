# 구구단_ex.py

# 구구단을 출력하는 프로그램
# 출력 형식

for dan in range(2, 10):
    for num in range(1, 10):
        print(f'{dan} * {num} = {dan * num}', end=' ')
    print(' ')


for num in range(1, 10):
    for dan in range(2, 10):
        print(f'{dan} * {num} = {dan * num}', end='\t|\t')
    print(' ')