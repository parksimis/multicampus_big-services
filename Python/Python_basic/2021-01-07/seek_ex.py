# seek_ex.py
print('----readline() 함수로 1행만 읽기----')
f = open('test2.txt', 'r')

f.seek(0, 0)
line = f.readline()
print(line, end='')
f.seek(0, 1)
line = f.readline()
print(line, end='')
f.seek(0, 1)
line = f.readline()
print(line, end='')
f.close()