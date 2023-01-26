def solution(X, A):
    positions = set()
    for i in range(len(A)):
        positions.add(A[i])
        if len(positions) == X:
            return i
    return -1