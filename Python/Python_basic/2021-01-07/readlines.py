# readlines.py

# realines() 함수 이용
# 리스트 형 반환

print('---- 전체 라인 읽고 출력 ----')

f = open('test.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()