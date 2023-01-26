"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time
results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
"""

def findMin(nums):
    # Input: nums = [4, 5, 6, 7, 0, 1, 2]
    # Output: 0
    l = 0
    r = len(nums) - 1

    # return result of array not rotated
    if nums[l] < nums[r]:
        return nums[l]

    # if rotated
    while l <= r:
        mid = (l + r) // 2

        # if on left side -> get to right, we know that the result must be there
        if nums[0] < nums[mid]:
            l = mid + 1

        # if number at mid-1 is smaller than the number at our current mid, we found the smallest number
        # we can return it
        elif nums[mid] < nums[mid-1]:
            return nums[mid]

        # if we are on the right side and we still have not found the smallest value
        # we need to look left of our current mid
        else:
            r = mid - 1



print(findMin([4, 5, 6, 7, 0, 1, 2]))
print(findMin([11,13,15,17]))
print(findMin([3,4,5,1,2]))
