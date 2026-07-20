def solution(n):
    answer = 0
    arr=[]
    for i in range(1,n//2 + 1):
        if n % i == 0:
            arr.append(i)
    if len(arr) % 2 == 0:
        return 1
    else:
        return 2