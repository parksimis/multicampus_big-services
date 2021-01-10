
alpha = number = spaces = etc = 0

phrase = input('문장을 입력하세요. : ')

for w in phrase:
    if w.isspace() == True:
        spaces += 1
    elif w.isdigit() == True:
        number += 1
    elif w.isalpha() == True:
        alpha += 1
    else:
        etc += 1
print(f'알파벳 : {alpha} 개 \n숫자 : {number} 개 \n스페이스 : {spaces} 개 \n기타 : {etc} 개')