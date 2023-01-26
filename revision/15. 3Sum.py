def threeSum(A):

    res = []

    # [-1, 0, 1, 2, -1, -4] -> [-4, -1, -1, 0, 1, 2]
    A.sort()

    # edge cases
    if len(A) < 3:
        return []

    i = 0

    while i < len(A)-1:
        l = i + 1
        r = len(A) - 1

        while l < r:
            three_sum = A[i] + A[l] + A[r]
            if three_sum > 0:
                r -= 1
            if three_sum < 0:
                l += 1
            if three_sum == 0:
                res.append([A[i], A[l], A[r]])
                l += 1
                while l < len(A) and A[l] == A[l - 1]:
                    l += 1

        i += 1
        while i < len(A) and A[i] == A[i - 1]:
            i += 1



    return res

print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([-2,0,1,1,2]))
print(threeSum([0,0,0,0]))