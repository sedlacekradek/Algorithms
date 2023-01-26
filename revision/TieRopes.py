def solution(K, A):
    res = 0
    temp_sum = 0

    for n in A:
        temp_sum += n
        if temp_sum >= K:
            res += 1
            temp_sum = 0

    return res