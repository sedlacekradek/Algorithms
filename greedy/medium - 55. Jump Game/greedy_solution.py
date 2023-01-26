"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""


def canJump(nums):
    # O(n)
    goal = len(nums) - 1

    # go through all numbers starting from the back
    # first value of range is included (len(nums)-1), second is not, so the last i value will not be -1 but 0
    for i in range(len(nums)-1, -1, -1):
        # if goal can be reached from this spot, shift the goal to this index
        # now if we are able to reach this index or further from any other field, we know we can reach the final goal
        if i + nums[i] >= goal:
            goal = i
    # if goal shifted all the way to index 0, return True
    return goal == 0


print(canJump([2, 3, 1, 1, 4]))





