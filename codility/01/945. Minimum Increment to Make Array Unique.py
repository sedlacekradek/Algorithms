"""
You are given an integer array nums. In one move, you can
pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
Return the minimum number of moves to make every value in nums unique.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

Example 2:
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
"""


def minIncrementForUnique(nums):
    # edge case
    if len(nums) == 0:
        return 0

    # sort O (n log n)
    nums.sort()

    result = 0
    min_val = 0

    for i in range(len(nums)):
        # if number higher than minimal val, we know we do not have to change it because we have a sorted array
        if i == 0 or nums[i] >= min_val:
            # update min_val
            min_val = nums[i] + 1
        else:
            # if number is lower than the min_val (aka the last evaluated value),
            # update the result
            # update min_val as in the previous case
            result += min_val - nums[i]
            min_val += 1

    return result

print(minIncrementForUnique([1,2,2]))
print(minIncrementForUnique([3,2,1,2,1,7]))