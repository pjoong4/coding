def solution(money):
    coffee_price = 5500
    answer = []
    coffee = money // coffee_price
    change_money = money % coffee_price 
    answer = [coffee, change_money]
    return answer