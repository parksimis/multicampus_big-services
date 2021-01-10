choose = input('도형 입력(1: 사각형, 2: 삼각형, 3: 원) : ')

PI = 3.14
shape = ""

if choose in ['1', '2', '3']:
    if choose == "1" or choose == "2":
        width = int(input('가로 입력'))
        height = int(input('세로 입력 : '))
        area = width * height

        if choose == "1":
            shape = '사각형'
        else:
            shape = '삼각형'
            area = area/2

    elif choose == '3':
        x = int(input('반지름 입력 : '))
        shape = '원'
        area = PI*x**2

    print(f'{shape}의 면적 = {area:.2f}')

else :
     print('1, 2, 3 중에 입력하세요.')


