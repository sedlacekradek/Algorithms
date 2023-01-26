"""
Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""


def eraseOverlapIntervals(intervals):
    # O (n log n)

    # list of intervals that we will keep, actually not needed we could just store the "lastEnd" value,
    # but could come handy in some other problems
    res_list = []
    res = 0
    # sort list based on the first value
    intervals.sort()
    # append the first interval
    res_list.append(intervals[0])

    # iterate through all intervals except the first one, which has already been appended
    for interval in intervals[1:]:
        # if intersecting
        if interval[0] < res_list[-1][1]:
            # update the result
            res += 1
            # keep only the interval with the lower second value
            if interval[1] > res_list[-1][1]:
                continue
            else:
                res_list.pop()
                res_list.append(interval)
        # if not intersecting, just append
        else:
            res_list.append(interval)
    return res

print(eraseOverlapIntervals(intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]))
print(eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals(intervals = [[1,2],[2,3]]))
print(eraseOverlapIntervals(intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))