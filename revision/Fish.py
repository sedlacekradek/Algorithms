def solution(A, B):
    res = 0
    max1 = float("-inf")
    max0 = float("-inf")

    for i in range(len(A)):
        if B[i] == 1:
            max1 = max(max1, A[i])
        else:
            if A[i] > max1:
                res += 1
                max1 = float("-inf")

    for i in range(len(A) - 1, -1, -1):
        if B[i] == 0:
            max0 = max(max0, A[i])
        else:
            if A[i] > max0:
                res += 1
                max0 = float("-inf")

    return res