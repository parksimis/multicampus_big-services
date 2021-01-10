# 내장함수기본.py

# abs(x) : x의 절댓값 반환
print(abs(-10))

# all(iterable) : 모든 요소가 참이면 True, 아니면 False 반환
# 파이썬은 0 : False로 처리 0이 아닌 모든 값 : True
# iterable : 반복 가능한 자료형 - for 문에 반복 요소로 사용할 수 있는 자료형
# Ex. 리스트, 튜플, dict, set

print(all([1, 2, 3]))
print(all([1, 2, 3, 'a']))
print(all([0, 2, 3, 'a'])) # False

# any(iterable) : 안에 들어있는 값이 하나라도 참이면 True, 모두 거짓이면 False 반환

print(any([1, 2, 3]))
print(any([1, 2, 3, 'a']))
print(any([0, 2, 3, 'a']))
print(any([0, 0, 0]))
print(any([0, '', []])) # 0, 빈문자열, 빈리스트 - False
print(any([None])) # None - False

# chr(i) : i 아스키코드를 전달 - 해당 아스키코드 값의 문자를 반환
print(chr(97))
print(chr(65))
print(chr(13))
print(chr(100))

# ord(c) : c는 문자 chr과 반대로 문자에 해당하는 아스키코드를 반환
print(ord('A'))
print(ord('b'))
print(ord('0'))
print(ord(' '))
print(ord('\n'))
print(ord('\r')) #13 : enter

# divmod(a, b) : a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
print(divmod(7, 3))

# enumerate(iterable, start=0)
# 시퀀스 (리스트, 튜플, 문자열, range)
# 인덱스값을 포함하는 enumerate 객체로 반환

print(enumerate(['kim', 'lee', 'park']))

# enumerate 객체의 각 요소 출력
for i, name in enumerate(['kim', 'lee', 'park']):
    print(i, name)

# for 문 처럼 반복되는 구간에서
# 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때, 유용하게 사용

# filter(function, iterable) : 반복 가능한 자료형 요소들이
# function에 전달되었을 때 반환값이 참인 것만 걸러내서 반환

def positive(x):
    # 반환 값이 True or False - 양수인 경우에 True
    return x > 0

print(filter(positive, [0, -1, 5, -7, 10]))
print(list(filter(positive, [0, -1, 5, -7, 10])))

# help([object]) : 내장 도움말 시스템을 호출

help(print)

# map(function, iterable)

def increase(x):
    return x+1

print(map(increase, [1, 2, 3, 4, 5])) # map 객체 형태로 넘어옴
print(list(map(increase, [1, 2, 3, 4, 5]))) # 결과값을 반환
print(list(filter(increase, [1, 2, 3, 4, 5]))) # 결과값의 참/거짓 여부 판단 후 출력

# open(filename, [mode]) : mode로 파일 열기
# mode(읽기 방법) 생략시 읽기 전용 모드(r:read)가 기본
# w(write), r(read), a(append), b(binary; 이미지) mode 존재

file_write = open('my_file.txt', 'w')

# sum(iterable) : iterable 모든 요소의 합 반환
print(sum([1, 2, 3, 4, 5]))

# zip(*iterable)
# 각 iterable에서 동일한 인덱스의 요소를 추출하여 묶어서(튜플) 형태로 반환

print(zip([1, 2, 3, 4], [5, 6, 7, 8])) #zip object 반환
print(list(zip([1, 2, 3, 4], [5, 6, 7, 8])))
print(list(zip([1, 2, 3, 4], [5, 6, 7]))) # 서로 길이가 다르면, 짝이 지어지지 않는 것은 제외하고 묶임
print(list(zip('123', 'abc')))

# zip() 함수를 사용해서 튜플로부터 딕셔너리를 생성하시오.
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)

result = dict(zip(keys, vals))
print(result)

print(int('11', 2)) # 문자열 11을 2진수 11변경 -> 10진수 3
print(int('A', 16)) # 문자열 A를 16진수 A변경 -> 10진수 10