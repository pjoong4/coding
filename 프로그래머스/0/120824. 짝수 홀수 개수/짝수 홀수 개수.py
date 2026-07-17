def solution(num_list):
    answer = []
    count_even = 0
    count_odd = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    answer = [count_even, count_odd]
    return answer