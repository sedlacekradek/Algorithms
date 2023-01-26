def solution(X, A):
    steps = set()
    for n in range(1, X + 1):
        steps.add(n)

    i = 0
    while len(steps) > 0 and i < len(A):
        if A[i] in steps:
            steps.remove(A[i])
        i += 1

    if len(steps) > 0:
        return -1

    return i - 1