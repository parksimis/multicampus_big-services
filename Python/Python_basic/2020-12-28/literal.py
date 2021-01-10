# 리터럴.py

# 정수 리터럴
a = 0b1010 # 2진수 리터럴
b = 300 # 10진수
c = 0o123 # 8진수
d = 0x12fc # 16진수

print(a, b, c, d) #10진수로 변환해서 출력

# 실수 리터럴
f1 = 3.14
f2 = -123.45
f3 = 1.234567e5

print(f1, f2, f3)

# 문자 리터럴
char = 'A'
char2 = "B"

# 문자열 리터럴
str1 = '홍길동'
str2 = "홍길동"
str3 = '''파이썬 프로그래밍'''
str4 = '제이름은'\
'길동'
str5 = '''여러줄로 
나누어서
출력해도 됨.'''
str6 = """ 큰 따온표를
세번 나열하면
삼중 따옴표가 됩니다."""
print(str6)

# 논리값 리터럴
t = True
f = False
print(t, f)

# 특수 리터럴
name = '홍길동' #문자열 리터럴
phone = None

print(name, phone)