def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    B.reverse()
    

    for i in range(len(B)):
        answer += A[i] * B[i]
                

    return answer