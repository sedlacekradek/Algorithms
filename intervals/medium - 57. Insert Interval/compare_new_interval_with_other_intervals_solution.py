"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

def insert(intervals, newInterval):
    # O(n)
    res = []

    # compare new interval with all other intervals that are sorted
    for i in range(len(intervals)):
        # if newinterval higher value is lower than the interval's lower value, we know the new interval
        # must be inserted before the current interval and we can return the result
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        # if the new interval's lower value is higher than the interval's higher value,
        # we know that these 2 intervals cannot intersect and we just append the current interval
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        # if the new interval intersects with the current interval, we calc the new values for the intersection
        # of these two intervals by using min/max functions, we do not append it to the result yet, because
        # our new interval may intersect with other following intervals as well
        else:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
    # append the new interval and return the result
    res.append(newInterval)
    return res

print(insert(intervals = [[1, 3], [6, 9]], newInterval = [2, 5]))
print(insert(intervals = [[1, 3], [6, 9]], newInterval = [10, 15]))
print(insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))

