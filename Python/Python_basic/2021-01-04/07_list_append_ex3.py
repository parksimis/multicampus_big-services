
product_list = []

while True:
    product = input('상품 등록 (엔터키를 누르면 종료) : ')
    if product == '':
        break
    else:
        product_list.append(product)

print('등록된 상품 : ', end='')
for i in range(len(product_list)):
    print(product_list[i], end=' ')