def twoSum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """

    i = 0

    while i < len(nums):
        x = i+1
        while x < len(nums):
            sum = nums[i] + nums[x]
            if sum == target:
                return [i, x]
            x += 1
        i += 1

# print(twoSum([2,7,11,15], 26))
print(twoSum([-1,-2,-3,-4,-5], -8))




