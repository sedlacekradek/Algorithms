def solution(A):
    res_set = set()
    for number in A:
        res_set.add(abs(number))
    return len(res_set)