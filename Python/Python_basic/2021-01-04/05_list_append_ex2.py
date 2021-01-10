
score_list = []
count = 0

number = int(input('학생 수 입력 : '))

for i in range(number):
    score = int(input(f'학생 {i+1} 점수 입력 : '))
    score_list.append(score)
    if score >= 80:
        count += 1
    else:
        pass

print(f'총점 : {sum(score_list)} \n평균 : {(sum(score_list)/len(score_list)):.2f} \n80점 이상인 학생의 수 : {count}')