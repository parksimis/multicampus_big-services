# 가변길이매개변수_kwargs

# key=value의 값을 받음 (dict 형태로 전달)

def show_keywords(**kwargs):
    print('-----------------')
    for key in kwargs.keys():
        print(key, end=' ')
    print('\n')

    for value in kwargs.values():
        print(value, end=' ')
    print('\n')

    for item in kwargs.items():
        print(item, end=' ')


show_keywords(id='sun',
              name='kim',
              phone='010-1234-1234')

# show_keywords(n1=2,
#               n2=2,
#               n3=3,
#               n4=4)

# key는 숫자형태를 쓸수 없다.
# show_keywards(1=2, 2=3, 3=4)