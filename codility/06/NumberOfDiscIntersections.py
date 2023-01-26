def fast_solution(A):
    # interval solution through counting simultaneously open intervals

    # edge case limit constant
    MAX_INTERSECTIONS = 10000000

    openings = []
    closings = []

    # create 2 lists with values when intervals open and close
    for i, n in enumerate(A):
        openings.append(i-n)
        closings.append(i+n)

    # O (n log n)
    openings.sort()  # -4, -1, 0, 0, 2 ,5
    closings.sort()  # 1, 4, 4, 5, 6, 8

    # count how many intervals are open at any point an interval is closed
    iopening = 0
    res = 0
    for iclosing in range(0, len(closings)):
        while iopening < len(openings) and openings[iopening] <= closings[iclosing]:
            iopening += 1

        res += iopening - iclosing - 1
        # check for edge case
        if res > MAX_INTERSECTIONS:
            return -1

    return res





print(fast_solution(([1, 5, 2, 1, 4, 0])))
print(fast_solution([1,1,1]))