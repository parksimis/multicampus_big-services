second = 1000

# 60으로 나눈 몫
minutes = second // 60

# 나머지
remainder = second % 60

print("{}분 {}초".format(minutes, remainder))


second = 10000

# 시간 계산
hour = second // 3600

# 시간 제외한 나머지 초
remainder = second % 3600

# 60으로 나눈 몫
minutes = remainder // 60

# 나머지
seconds = remainder % 60

print("{}시간 {}분 {}초".format(hour, minutes, seconds))