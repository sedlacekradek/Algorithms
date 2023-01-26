def solution(A, B, K):
    for n in range(A, B+1):
        if n % K == 0:
            difference = B - n
            res = (difference // K) + 1
            return res
    return 0