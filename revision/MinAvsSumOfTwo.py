def solution(a):

    # edge cases
    if len(a) == 1:
        return abs(sum(a) * 2)

    a.sort()
    if a[0] >= 0:
        return 2 * a[0]
    if a[len(a)-1] <= 0:
        return abs(a[-1] * 2)

    l = 0
    r = len(a) - 1
    min_sum = float('inf')

    while l <= r:
        min_sum = min(min_sum, abs(a[l] + a[r]))
        if abs(a[l]) > abs(a[r]):
            l += 1
        else:
            r -= 1
    return min_sum