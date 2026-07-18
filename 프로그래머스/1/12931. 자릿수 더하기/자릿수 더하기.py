def solution(n):
    answer = 0
    num = 1
    
    while num <= 100000000:
        digit = n % (num*10) // num
        num *= 10
        answer += digit
    return answer