def solution(n):
    answer = 0
    x = 1
    while n >= x:
        if (n // x == x) and (n % x == 0):
            answer = (x+1) * (x+1)
            break
        else:
            answer = -1
            x += 1
        
    return answer