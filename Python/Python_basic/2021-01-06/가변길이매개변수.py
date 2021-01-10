
def test_args(*args):
    print(type(args))

test_args(1, 2, 3, 4, 5)

def test_kwargs(**kwargs):
    print(type(kwargs))

test_kwargs(a=1, b=2, c=3)

def order_coffee(coffee, *options):
    print(coffee + ', 옵션 : ', end=' ')

    for opt in options:
        print(opt, end=' ')
    print()


order_coffee('아메리카노')
order_coffee('아메리카노', 'Tall', 'Hot', '시럽')
#order_coffee()

def order_coffee_1(coffee, *options, fin='end'):
    print(coffee + ', 옵션 : ', end=' ')

    for opt in options:
        print(opt, end=' ')
    print(fin)


order_coffee_1('아메리카노')
order_coffee_1('아메리카노', 'Tall', 'Hot', '시럽')

def order_coffee_2(coffee, fin='end', *options):
    print(coffee + ', 옵션 : ', end=' ')

    for opt in options:
        print(opt, end=' ')
    print(fin)


order_coffee_2('아메리카노')
order_coffee_2('아메리카노', 'Tall', 'Hot', '시럽')
