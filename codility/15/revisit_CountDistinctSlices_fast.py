def solution(M, A):
    s = 0
    res = 0
    hash_set = set()

    for f in range(len(A)):
        while A[f] in hash_set:
            hash_set.remove(A[s])
            s += 1
        res += f - s + 1
        if res >= 1000000000:
            return 1000000000
        hash_set.add(A[f])
    return res