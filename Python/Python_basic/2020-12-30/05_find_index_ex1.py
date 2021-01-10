# 이메일 형식이 아닌 경우
# @, .이 없는 경우
# @과 .위치가 바뀐 경우 @과 .사이에 문자가 없는 경우

email = input('이메일을 입력 : ')

if email.count('@') != 1 or email.count('.') >= 3 :
    print(f'이메일 형식이 아닙니다. \n 입력한 이메일 {email}')
elif email.find('@') > email.find('.') or\
    abs(email.find('@') - email.find('.')) == 1:
    print(f'이메일 형식이 아닙니다. \n 입력한 이메일 {email}')
elif email[email.find('.')] == email[-1] or\
        email[email.find('@')] == email[0]:
    print(f'이메일 형식이 아닙니다. \n 입력한 이메일 {email}')
else:
    print(f'옳은 이메일 형식입니다. \n 입력한 이메일 {email}')