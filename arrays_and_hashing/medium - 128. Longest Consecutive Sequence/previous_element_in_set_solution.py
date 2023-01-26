"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


def longestConsecutive(nums):
    nums = set(nums)
    res = 0

    for number in nums:
        # if number -1 in array, it means that the number is not the first element of consecutive row and we can
        # move on until we find the first element
        if number -1 in nums:
            continue
        else:
            # when first element found
            # check if the row can be longer than the one already found
            if number + res in nums:
                counter = 1
                # while number +1 in array, keep adding to counter
                while number + 1 in nums:
                    counter += 1
                    number += 1
                # if counter higher than the highest counter so far, update result
                if counter > res:
                    res = counter
    return res




print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([0]))
print(longestConsecutive([]))