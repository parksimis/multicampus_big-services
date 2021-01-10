# 파일생성.py

# 파일 생성 : 파일명만 적으면 현재 디렉터리에 생성

f = open('file.txt', 'w') # f 변수에 파일을 참조할 수 있는 포인터
f.close() # f가 가리키고 있는 file을 닫음.

# w 모드는 해당 파일이 없으면 생성
# 해당 파일이 존재하면 기존 파일을 초기화(덮어쓰기)한다. 기존 내용은 삭제된다.

# 존재하지 않는 디렉터리에 생성하면 에러
#f = open('c:/python/file1.txt', 'w') # 현재 폴더외 다른 폴더에 파일을 만들고 싶으면 전체 경로를 적는다.
# FileNotFoundError: [Errno 2] No such file or directory: 'c:/python/file1.txt'
#f.close()

f = open('c:/PythonStudy/file.txt', 'w')
f.close()

# 경로에 \를 쓰려면 \\ 또는 앞에 r을 붙임

f = open(r'C:\PythonStudy\file1.txt', 'w')
f.close()

# 파일에 data 쓰기 : 파일을 쓰기모드(w)로 열고
# 파일 객체의 write()함수로 값을 파일에 기록
data = 'hi'
f = open(r'C:\PythonStudy\file2.txt', 'w')
f.write(data) # 파일에 data 쓰기
f.close()

