def solution(A, K):
    if A == []:
        return []

    shift_by = K % len(A)
    res = [[] for _ in range(len(A))]

    for i in range(len(A)):
        new_index = i + shift_by
        while new_index > len(A) - 1:
            new_index -= len(A)
        res[new_index] = A[i]

    return res

print(solution([], 0))