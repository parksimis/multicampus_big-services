# 키워드인수.py

# 위치인수 : 나열한 순서대로 매개변수에 전달되는 인수(위치값으로 전달될 변수를 정함)
# add(1, 2, 3) -> 1은 첫번째 매개변수로, 3은 마지막 매개변수로 전달

# 키워드 인수 : 인수들앞에 키워드를 두어서 인수를 구별하는 방식
# add(a=1, c=3, b=2) -> 각 인수앞에 키워드에 해당하는 변수로 전달(순서를 바꿔도 됨)

def student_info(name, age, gender):
    student = {
        'name' : name,
        'age' : age,
        'gender' : gender
    }
    return student


print(student_info('kim', 23, '여')) # 위치 인수
print(student_info(age=23, name='kim', gender='여')) # 키워드 인수
print(student_info('lee', gender='남', age=22)) # 혼용 사용

#print(student_info( gender='남', age=22,'lee')) # 혼용 사용시 위치 인수가 키워드 인수보다 뒤로 가면 안됨.

