# 현금이 5,000원이 있고, 사탕 가격이 120원인 경우
# 최대한 살 수 있는 사탕의 개수와 나머지 돈은 얼마인가?

myMoney = 5000
candyPrice = 120
numCandies = myMoney // candyPrice
change = myMoney % candyPrice

print("사탕의 개수 : {} 개 \n나머지 돈 : {} 원 ".format(numCandies, change))