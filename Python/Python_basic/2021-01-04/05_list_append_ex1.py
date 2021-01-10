name_list = []

for i in range(3):
    name = input('회원 입력 : ')
    name_list.append(name)

print('회원 명단 : ', end=' ')
for i in range(len(name_list)):
    print(name_list[i], end=' ')