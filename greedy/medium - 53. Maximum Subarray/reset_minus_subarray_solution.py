"""
Given an integer array nums, find the
subarray which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""

def maxSubArray(nums):
    # O(n)
    res = 0
    total = 0

    for n in nums:
        # update total
        total += n
        # if total highest so far, updated result
        res = max(total, res)
        # if total a minus value, reset to 0 a keep iterating
        if total < 0:
            total = 0
    return res

print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
