def merge(intervals):
    intervals.sort()
    res = []
    current = []

    for interval in intervals:
        if current == []:
            current = interval
        elif current[1] < interval[0]:
            res.append(current)
            current = interval
        else:
            current = [current[0], max(current[1], interval[1])]

    if current not in res:
        res.append(current)

    return res