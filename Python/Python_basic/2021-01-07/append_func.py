# append_func.py

# append() : 파일 끝에 데이터를 추가
# 파일 열기 모드 : a (append)

f = open('test2.txt', 'a')

ap_data = '\n\nPython Programming'
f.write(ap_data) # append 모드이므로 파일 끝에 데이터를 추가

f = open('test2.txt', 'r')
print(f.read())

f.close()