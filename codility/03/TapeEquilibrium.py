def solution(A):
    # sum all elements of A
    a_sum = sum(A)
    res = float("inf")
    # set initial minus_val, we will iterate from index 1 so we will set minus_val as 2x A[0]
    minus_val = A[0] * 2

    for n in range(1, len(A)):
        temp = abs(a_sum - minus_val)
        res = min(res, temp)
        # not to forget to multiply by 2 (subtract from the right size + add it to the left side)
        minus_val += A[n] * 2

    return res