"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


def containsDuplicate(nums):
    # time complexity O(n)
    hash_table = set()
    for n in nums:
        if n in hash_table:
            return True
        else:
            hash_table.add(n)
    return False


print(containsDuplicate([1,2,3,4]))
