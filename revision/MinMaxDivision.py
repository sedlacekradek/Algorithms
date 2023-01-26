def solution(K, M, A):
    res = float("inf")
    low = max(A)
    high = sum(A)

    while low <= high:
        subsum = (low + high) // 2
        mysum = 0
        counter = 0
        for n in A:
            mysum += n
            if mysum == subsum:
                mysum = 0
                counter += 1
            elif mysum > subsum:
                mysum = n
                counter += 1
        if mysum != 0:
            counter += 1
        if counter > K:
            low = subsum + 1
        else:
            res = min(res, subsum)
            high = subsum - 1

    return res