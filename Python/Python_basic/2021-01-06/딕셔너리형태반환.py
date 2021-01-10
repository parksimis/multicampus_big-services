# 딕셔너리형태반환.py

product_list = [{'name' : '노트북', 'price' : 1200000 },
                {'name' : '냉장고', 'price' : 1700000 }] # 리스트에 딕셔너리를 포함하는 구조

# 딕셔너리를 전달받아서
# 일부만 추출해서 딕셔너리 형태로 반환하는 함수

def get_product_inf(prd_dic):
    name = prd_dic['name']
    price = prd_dic['price']
    return {'no1' : name, 'no2' : price}

# 리스트에서 딕셔너리를 함수에 전달
# 반환값 받아서 출력

for prd in product_list:
    prd_info = get_product_inf(prd)
    print(prd_info)
