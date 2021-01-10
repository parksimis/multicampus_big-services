choose = input('도형 입력(1: 사각형, 2: 삼각형, 3: 원) : ')

PI = 3.14

if choose == "1" or choose == "2":
    width = int(input('가로 입력'))
    height = int(input('세로 입력 : '))
    area = width * height

    if choose == "1":
        print('사각형의 면적 : ', area)
    else:
        print('삼각형의 면적 : ', area/2)

else:
    x = int(input('반지름 입력 : '))
    area = PI*x**2
    print('원의 면적 = ', area)