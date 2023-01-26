def twoSum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """

    seen = {}
    # enumerate to iterate through both index and value
    for i, value in enumerate(nums):
        # calc which value we are looking for to get solution
        remaining = target - value

        # if we have not come across this value yet
        if remaining not in seen:
            # add value and index to the hash table
            seen[value] = i
        # if we have already come across the value
        else:
            # return correct solution
            return [i, seen[remaining]]

# print(twoSum([2,7,11,15], 26))
print(twoSum([-1,-2,-3,-4,-5], -8))