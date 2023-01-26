"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
"""

def jump(nums):
    l = 0
    r = 0
    res = 0
    jump = 0

    # 2 pointers marking the range where we can jump from a given spot
    while r < len(nums) - 1:
        # for each number in the range, check which is the furthest spot we can jump
        for n in range(l, r+1):  # r+1 because we want the right side of the range to also be included
            jump = max(jump, n + nums[n])
        # shift the 2 pointers, L will always be the very next spot from the last R
        l = r + 1
        # R will be the furthest spot we can jump to
        r = jump
        # update result
        res += 1
    return res






print(jump([2,3,1,1,4]))
print(jump([1,2]))
print(jump([2,3,1]))

