"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def merge(intervals):
    # O(n log n) -> because sorting is needed

    # sort and create a res variable
    intervals.sort()
    res = []

    # append first (lowest) interval to res
    res.append(intervals[0])

    # iterate through, skip the interval at index 0 as it is already added in res
    for interval in intervals[1:]:
        # compare interval with most recently added interval -> res[-1]
        # if intervals intersect
        if interval[0] <= res[-1][1]:
            # calc values of the new interval
            val0 = min(interval[0], res[-1][0])
            val1 = max(interval[1],res[-1][1])
            # change value of the most recently added interval
            res[-1] = [val0, val1]
        # if intervals do not intersect, update res with the next interval
        else:
            res.append(interval)
    return res


print(merge([[1, 3], [8, 10],  [2, 6], [15, 18]]))


