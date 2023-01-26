"""
Given an array of meeting intervals, determine if a person could attend all meetings.

Example 1:
intervals = [(0,30),(5,10),(15,20)]
output: False
There is a conflict
"""

def check_meetings(intervals):
    intervals.sort()
    last_end = intervals[0][1]

    for interval in intervals[1:]:
        if interval[0] < last_end:
            return False
        else:
            last_end = interval[1]
    return True

print(check_meetings(intervals = [(0,30),(5,10),(15,20)]))
print(check_meetings(intervals = [(0,30),(30,45),(50,120)]))