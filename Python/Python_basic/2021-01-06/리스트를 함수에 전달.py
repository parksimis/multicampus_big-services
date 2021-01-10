# 리스트를 함수에 전달

# 매개변수의 값으로 리스트를 전달했을 경우

def show_list(my_list): # 매개변수 my_list - 지역변수
    print('전달된 리스트 변경 없음', my_list) # 변경 전 전달 내용 출력
    my_list[0] = 10 #첫번째 요소 변경
    print('첫번째 요소 변경 후', my_list)
    print('1. id(함수 내-매개변수) :', id(my_list)) # id는 변수가 생성된 메모리 주소 반환
    # 함수 바깥의 전역변수(my_list)와 id가 동일함
    ### 전체 리스트에 새로운 값을 저장 시
    ### 원본 리스트의 전체 요소가 변경되는 것이 아니라
    my_list = [100, 200, 300] # 새로운 리스트를 생성 - 공간도 새로 차지하게 됨
    print('함수 내에서 my_list의 전체 값을 다시 저장')
    print(my_list) # [100, 200, 300]
    print('3. id(함수 내-매개변수) :', id(my_list)) # 새로운 id가 출력


my_list = [1, 2, 3, 4] # 함수 바깥에서 변수 선언 - 전역 변수
print('함수 호출 전')
print(my_list)
print('함수 호출')
show_list(my_list)
print('함수 호출 후 ')
print(my_list)
print('2. id(함수 바깥-전역변수) :', id(my_list)) # 함수 내 매개변수와 동일한 id

# -> 함수에서 리스트 요소 변경 시 원본 리스트도 변경됨

# 리스트를 매개변수로 전달하면 함수 내에서나 함수 외부에서 동일한 리스트를 사용하게 된다.
# 전달된 리스트 요소의 일부를 함수 내에서 변경하면 원본 리스트도 동일하게 변경된다.
# 단, 함수 내에서 변수=[값1, 값2, 값3] 와 같이 리스트를 생성하면, 해당변수는 완전한 지역변수로 처리된다.
