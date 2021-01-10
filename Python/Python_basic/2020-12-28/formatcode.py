# 포맷 코드
# %s 문자열
# %c 문자 1개
# %d 정수
# %f 부동 소수
# %o 8진수
# %x 16진수
# %% % 그 자체

name = '홍길동'
no = '2016001'
year = 4
grade = 'A'
average = 93.5

print("성명 : %s" % name)
print("number : %s" % no)
print("학년 : %d" % year)
print("학점 : %s" % grade)
print("평균 : %.2f" % average)

# 퍼센트 문자열을 출력
print('10%')

rate = 80

print("출석률 : %d%%" % rate)