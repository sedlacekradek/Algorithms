def solution(A):
    count = 0
    res = 0

    for i in range(len(A) - 1, -1, -1):
        if A[i] == 1:
            count += 1
        else:
            res += count
        if res > 1000000000:
            return -1

    return res