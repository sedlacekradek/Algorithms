def solution(A, B):
    # scores 50%; fails all time complexity checks
    # works even if the intervals are not given in any sorted manner
    intervals = []

    for a, b in zip(A, B):
        intervals.append((a, b))

    if len(intervals) == 0:
        return 0

    intervals.sort()

    res = 1

    for i in range(len(intervals) - 1):
        j = i + 1
        if res > len(intervals) - j:
            return res
        counter = 1
        interval_end = intervals[i][1]

        for y in range(j, len(intervals)):
            if intervals[y][0] > interval_end:
                interval_end = intervals[y][1]
                counter += 1
                res = max(res, counter)

    return res

print(solution([1,2,4,6],[99,3,5,7]))