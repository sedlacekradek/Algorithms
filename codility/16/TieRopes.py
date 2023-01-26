def solution(K, A):
    res = 0
    rope = 0

    for n in A:
        rope += n
        if rope >= K:
            res += 1
            rope = 0

    return res