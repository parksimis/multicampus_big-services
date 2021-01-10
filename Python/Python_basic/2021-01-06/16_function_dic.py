# 16_function_dic.py

def show_info(name, year, age, phone):
    info = {'name' : name,
            'year' : year,
            'age' : age,
            'phone': phone}

    return info

# main
print(show_info('홍길동', 4, 23, '010-1234-1234'))