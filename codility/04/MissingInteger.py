def solution(A):
    A = set(A)

    for n in range(1, 1000001):
        if n not in A:
            return n