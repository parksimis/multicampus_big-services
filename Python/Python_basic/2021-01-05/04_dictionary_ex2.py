dictionary = {}

while True:
    word = input('영어 단어 등록 (종료는 quit) : ')
    if word in dictionary:
        print(f'{word}는 이미 등록된 단어 입니다.')
    elif word == 'quit':
        print('종료합니다.')
        break
    else:
        meaning = input(f'{word}의 뜻입력 (종료는 quit) : ')
        dictionary[word] = meaning

while True:
    word = input('검색할 단어 등록 (종료는 quit) : ')
    if word in dictionary:
        print(f'{word}의 뜻은 {dictionary[word]}입니다.')
    elif word == 'quit':
        print('종료합니다.')
        break
    else:
        print(f'{word}는 사전에 없는 단어 입니다.')