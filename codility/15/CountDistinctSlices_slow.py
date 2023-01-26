def solution(M, A):
    s = 0
    res = 0

    while s < len(A):
        hash_set = set()
        f = s
        while f < len(A):
            if A[f] not in hash_set:
                res += 1
                hash_set.add(A[f])
                f += 1
            else:
                break
        s += 1
    return res