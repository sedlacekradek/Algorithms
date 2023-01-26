def solution(A, B):
    # this solution works because the intervals are by default sorted in ascending order by their ending (B) value
    n = len(A)

    last_b = -1
    result = 0
    for index in range(n):
        if A[index] > last_b:
            result += 1
            last_b = B[index]

    return result
