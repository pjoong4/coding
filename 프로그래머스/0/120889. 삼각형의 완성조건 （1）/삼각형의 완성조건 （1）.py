def solution(sides):
    answer = 0
    count = 0
    for i in range(len(sides)):
        if sides[i] < sides[i-1] + sides[i-2]:
            count += 1
    if count == 3:
        answer = 1
    else:
        answer = 2
    return answer