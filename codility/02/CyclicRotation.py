def solution(A, K):
    res = [[] for _ in range(len(A))]

    # time complexity O (n)
    # extra space complexity O (n)
    for index, number in enumerate(A):
        new_index = (index + K) % len(A)
        res[new_index] = number

    return res

print(solution([3, 8, 9, 7, 6], 3 ))