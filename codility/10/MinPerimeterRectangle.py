def solution(N):
    i = 1
    max_div = 0

    while i * i <= N:
        if N % i == 0:
            max_div = max(max_div, i)
        i += 1

    res = 2 * (max_div + int(N / max_div))

    return res 