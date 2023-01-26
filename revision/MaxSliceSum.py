def solution(A):
    res = 0
    subsum = 0

    a_max = max(A)
    if a_max <= 0:
        return a_max

    for n in A:
        subsum = max(subsum + n, 0)
        res = max(subsum, res)
    return res