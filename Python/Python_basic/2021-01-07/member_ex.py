# member_ex.py

with open('member.csv', 'w') as file:

    while True:
        name = input('이름 입력 : 종료하려면 이번 입력에서 quit를 입력하세요.')
        if name == 'quit':
            print('입력을 종료합니다.')
            break
        else:
            birth = input('생년월일 입력 : ')
            address = input('주소 입력 : ')

            data = name + ',' + birth + ',' + address + '\n'
            file.write(data)





