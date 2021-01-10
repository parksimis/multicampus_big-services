# 파일에데이터쓰기.py

# 파일에 한글 쓰기 - 한글 인코딩 문제

# 파일에 data 보내기(쓰기) : 파일을 쓰기 모드(w)로 열고
# 파일 객체의 write()함수로

data = '안녕하세요'
f = open('file1.txt', 'w', encoding='utf-8')
f.write(data) # 파일에 data 쓰기
f.close()

# 파일에 여러 행 데이터 쓰기('\n')
f = open('file2.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    data = f'{i}행\n'
    f.write(data)

f.close()