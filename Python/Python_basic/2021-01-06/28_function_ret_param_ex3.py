# 매개변수 연습문제 2

def order(price, qty):
    amount = price * qty
    if amount >= 100000:
        discount = amount * 0.1
    elif amount >= 50000:
        discount = amount * 0.05
    else:
        discount = 0

    total = amount - discount

    return int(amount), int(discount), int(total)

price = int(input('상품 가격 입력 : '))
qty = int(input('주문 수량 입력 : '))
print('------------------------------------')
amount, discount, total = order(price, qty)
print(f'주문액 : {amount}원')
print(f'할인액 : {discount}원')
print(f'지불액 : {total}원')