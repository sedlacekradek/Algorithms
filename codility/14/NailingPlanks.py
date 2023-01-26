# scores 50%

def check_possible(mid, A, B, C):
    i = 0
    j = 0
    counter = 0
    while i < len(C) and j < len(A):
        if C[i] < A[j] or C[i] > B[j]:
            counter += 1
            i += 1
        else:
            j += 1
    return counter < mid


def solution(A, B, C):
    low = 1
    high = len(C)
    res = -1

    while low <= high:
        mid = (low + high) // 2
        if check_possible(mid, A, B, C):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res