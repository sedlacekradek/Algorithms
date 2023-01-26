def solution(N):
    factors = set()
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            factors.add(i)
            factors.add(N // i)
    return len(factors)