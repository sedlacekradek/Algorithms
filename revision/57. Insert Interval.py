def insert(intervals, new):
    res = []

    for interval in intervals:
        if new and new[1] < interval[0]:
            res.append(new)
            new = None

        if new and new[0] <= interval[1]:
            new = [min(new[0], interval[0]), max(new[1], interval[1])]
        else:
            res.append(interval)

    if new and new not in res:
        res.append(new)

    return res
