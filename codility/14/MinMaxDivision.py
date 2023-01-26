def count_blocks(mid, A, K):
    current_sum = 0
    result = 1
    for n in A:
        if current_sum + n > mid:
            result += 1
            current_sum = n
            continue
        current_sum += n
    return result <= K


def solution(K, M, A):
    low = max(A)
    high = sum(A)
    res = float("inf")

    if K == 1:
        return high

    # search for the possible minimal sum using binary search
    while low <= high:
        mid = (low + high) // 2
        # search if using this sum we do not overreach the maximum number of blocks
        if count_blocks(mid, A, K):
            # if possible result, save it and try a lower sum
            res = mid
            high = mid - 1
        else:
            # if result not possible (too many blocks), increase the possible sum and try again
            low = mid + 1
    return res

print(solution(3, 5, [2, 1, 5, 1, 2, 2, 2])) # 6
print(solution(1, 1, [0])) # 0
print(solution(1, 10, [5, 3])) # 8
print(solution(2, 10, [5, 3])) # 5
print(solution(3, 6, [5, 2, 3, 4, 6])) # 7 not 6