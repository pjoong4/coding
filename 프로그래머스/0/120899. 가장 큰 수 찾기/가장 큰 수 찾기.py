def solution(array):
    answer = []
    temp_array = array.copy()
    temp_array.sort()
    answer.append(temp_array[len(temp_array)-1])
    answer.append(array.index(answer[0]))
    return answer