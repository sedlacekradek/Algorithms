def solution(A):
    A.sort()

    if (A[0] * A[1]  * A[-1]) > (A[-3] * A[-2]  * A[-1]):
        return A[0] * A[1]  * A[-1]
    else:
        return A[-3] * A[-2]  * A[-1]