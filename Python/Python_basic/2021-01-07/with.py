# with.py

# 파일을 자동으로 close하는 등 관리를 해주는 문장이 있다. 이것이 with 문임

# with open(파일명, 열기모드) as 파일객체변수명:
#   처리 코드

# with문이 종료되면 파일 객체는 자동으로 close()

with open('test3.txt', 'w') as f:
    f.write('hello')

# 변수로 처리
file = 'test4.txt'
data = '''Python programming
R programming
Web programming'''

with open(file, 'w') as f:
    f.write(data)
    