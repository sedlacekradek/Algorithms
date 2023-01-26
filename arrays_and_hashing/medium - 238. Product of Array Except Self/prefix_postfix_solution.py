"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

def productExceptSelf(nums):
    """
    create two lists:
        prefix_list - product of all numbers pre-index
        postfix_list - product of all numbers post-index
    final product = prefix_list number * postfix_list number
    """

    prefix = 1  # default prefix value must be 1 -> 0 would give always 0 result
    postfix = 1  # same for postfix
    prefix_list = []

    # create postfix list and index value
    # this list will be populated from the back
    postfix_list = [[]for _ in range(len(nums))]
    i = len(nums) - 1

    # populate prefix list
    for number in nums:
        prefix_list.append(prefix)
        prefix = prefix * number

    # populate postfix list
    for number in nums[::-1]:
        postfix_list[i] = postfix
        postfix = postfix * number
        i -= 1

    # get result by prefix * postfix
    for i in range(len(nums)):
        nums[i] = prefix_list[i] * postfix_list[i]

    # print(prefix_list)
    # print(postfix_list)
    return nums

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))