def solution(x):
    answer = True
    digits = 1
    count = 1
    value = 0
    
    while x // digits != 0:
        value += x % (digits*10) // (digits)
        digits *= 10
        
    if x % value != 0:
        answer = False
        
    return answer