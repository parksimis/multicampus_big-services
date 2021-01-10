# 다중 for 문을 사용하여 다음과 같이 출력
sum = 0
for i in range(3):
    for j in range(1, 5):
        sum += 1
        print(sum, end='\t')
    print("")
