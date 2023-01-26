def solution(A):
    zero_count = 0
    res = 0

    for n in A:
        if n == 0:
            zero_count += 1
        else:
            res += zero_count
            if res > 1000000000:
                return -1

    return res