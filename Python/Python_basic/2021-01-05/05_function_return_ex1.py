def get_area():
    height = int(input('가로 길이 입력 : '))
    width = int(input('세로 길이 입력 : '))
    return height * width


area = get_area()
print('사각형의 면적 : ', area)