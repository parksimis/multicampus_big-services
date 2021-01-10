
def get_interest(deposit, int_rate):
    interest = deposit * int_rate/100
    interest = format(int(interest), ',')
    return interest



# main
deposit = int(input('예금액 입력 : '))
int_rate = float(input('이자율 입력(%) : '))

interest = get_interest(deposit, int_rate)
print(f'이자액 : {interest}원')