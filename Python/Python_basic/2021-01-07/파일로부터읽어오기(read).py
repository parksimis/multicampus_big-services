# 파일로부터 읽어오기(read).py

# readline()
# 1개 행 읽어오기
# 1행 끝에 '\n'을 포함

# readlines()
# 모든 행을 읽어 라인별로 잘라서 리스트로 생성 후 반환
# 그 리스트에는 1개 행이 1개의 요소로 들어가 있음

# read()
# 내용 전체를 읽어서 문자열로 반환

print('----------------첫번째 행 읽기----------------')
f = open('test.txt', 'r')
line = f.readline() # 첫번째 라인 1개 읽기
print(f'{line}\n끝입니다')
f.close()

#readline() 함수를 이용해 전체 라인 읽어오는 코드
print('----------------파일 전체 읽기----------------')
f2 = open('test.txt', 'r')

while True:
    line = f2.readline() # 라인 1개 읽고 포인터를 다음행으로 이동
    if not line :
        break
    else:
        print(line, end='')

f2.close()
