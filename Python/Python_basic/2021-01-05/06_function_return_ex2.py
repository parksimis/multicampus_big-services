

def order():
    price = int(input('상품가격 입력 : '))
    amount = int(input('주문 수량 입력 : '))

    return price, amount, price*amount

price, amount, total = order()
print('-------------------------------')
print(f'상품가격 : {price} \n주문수량 : {amount} \n주문액 : {total}')