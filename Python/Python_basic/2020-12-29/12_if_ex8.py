# 다음과 같이 프로그램 작성(중첩 if 사용)

number = int(input('번호 입력 (1.현금 2.카드) : '))

if number == 1 or number == 2:
    cost = int(input('지불액 입력 : '))
    if number == 1:
        print('할인율 10 %')
        print('할인액 : {} 원'.format(int(cost*0.1)))
    else:
        print('할인율 5 %')
        print('할인액 : {} 원'.format(int(cost * 0.05)))
else:
    print('잘못 입력했습니다. 종료합니다.')