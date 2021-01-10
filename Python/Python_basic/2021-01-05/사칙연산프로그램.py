def calc(op, n1, n2):
    result = 0
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    else:
        result = n1 / n2

    return result


# main
while True:
    op = input('연산자 입력 (+, -, *, / 중 하나)')
    n1 = int(input('숫자 1 입력'))
    n2 = int(input('숫자 2 입력'))
    if op not in ['+', '-', '*', '/']:
        print('연산자 오류! 다시 입력하세요.')
    elif (op == '/') and (n2 == 0):
        print('0으로 나눌 수 없습니다. 다시 입력하세요.')
    else:
        result = calc(op, n1, n2)
        print(f'{n1} {op} {n2} = {result}')
        break