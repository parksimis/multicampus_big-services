# for1_누적합.py

# 1부터 10까지 출력하고, 1부터 10까지 더한 결과를 마지막에 출력
sum = 0
for i in range(1, 11):
    print(i)
    sum += i

print('1부터 10까지의 누적합', sum)

sum = 0
for j in range(1, 101, 2):
    print(j)
    sum += j

print('1부터 100까지의 누적합', sum)