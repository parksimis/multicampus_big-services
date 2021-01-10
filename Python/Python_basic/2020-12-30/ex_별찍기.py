
# 다중 for문 실습
# 별로 트리만들기

for i in range(4):
    for j in range(5):
        print('*', end='')
    print('')

print('------------------------')

for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end='')
    print('')

print('------------------------')

for i in range(1, 6):
    for j in range(i, 6):
        print('*', end='')
    print('')