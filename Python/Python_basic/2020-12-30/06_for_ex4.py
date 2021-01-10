# 구구단의 단수를 입력받아 해당 구구단 출력

n = int(input("단 입력 : "))

for i in range(1, 10):
    print(f'{n}\t*\t{i}\t=\t{n*i}')