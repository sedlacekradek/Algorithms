def solution(A):
    count = {}
    min_val = len(A) // 2

    for i, n in enumerate(A):
        count[n] = count.get(n, 0) + 1
        if count[n] > min_val:
            return i

    return -1