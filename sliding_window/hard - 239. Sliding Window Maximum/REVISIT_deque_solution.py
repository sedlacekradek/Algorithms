"""
You are given an array of integers nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""


def maxSlidingWindow(nums, k):
    # brutal force solution not possible due to high time complexity that results into a timeout error

    # Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    # Output: [3, 3, 5, 5, 6, 7]

    from collections import deque
    output = []
    q = deque()  # index
    l = r = 0
    # O(n) O(n)
    while r < len(nums):
        # pop smaller values from q
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # remove left val from window
        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output


print(maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(maxSlidingWindow(nums = [1,-1], k = 1))
