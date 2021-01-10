# seek.py

# 파일 내에서 검색(위치 이동)
# seek(offset, whence) 함수

print('---- 파일 내에서 검색 : seek() ----')

f = open('test2.txt', 'r')
f.seek(0, 0) # 시작위치 (offset, 위치) : 파일의 시작점에서 0번째 문자
# (0, 0): 0 행 0 열 (파일 시작 위치)

# 파일 전체 읽어오기(리스트 반환)
lines = f.readlines()
print(lines) # 리스트로 출력

# 포인터 위치 변경
f.seek(1, 0) # offset 1, 위치 문서 처음 : 문서 처음에서 하나 옆으로 간 것
lines = f.readlines()
print(lines)

# 두번째 행부터 읽어오기
f.seek(7, 0) # offset 7, 위치 문서 처음 : 문서 처음에서 하나 옆으로 간 것
lines = f.readlines()
print(lines)

# 한글은 2바이트
# 시작위치부터 offset 14부터 읽어오기
f.seek(14,0)
lines = f.readlines()
print(lines)

f.seek(16,0) # 세번째 행 두 번째 글자 (한글이므로 이전 글자 위치에서 2씩 증가시켜야함 -> 1 증가시키면 에러)
lines = f.readlines()
print(lines)
f.close()

