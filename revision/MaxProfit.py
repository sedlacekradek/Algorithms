def solution(A):
    res = 0

    if A == []:
        return res

    min_price = A[0]

    for n in A[1:]:
        profit = n - min_price
        res = max(res, profit)
        min_price = min(min_price, n)

    return res