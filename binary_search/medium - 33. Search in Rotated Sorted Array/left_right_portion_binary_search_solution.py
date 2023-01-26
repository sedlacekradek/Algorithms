"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot
index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index
of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
"""

def search(nums, target):
    # Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    # Output: 4
    # hidden info: rotated at pivot index 3
    l = 0
    r = len(nums) - 1

    while l <= r:
        # if target found
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        # we are on the left side
        if nums[l] <= nums[mid]:
            # if on left side and target > mid, we know we must search right from mid
            if target > nums[mid]:
                l = mid + 1
            # if target is lower than the leftmost value, we know we must look for our target right from mid
            elif target < nums[l]:
                l = mid + 1
            # target less than middle but greater than left (target < nums[mid] and target > nums[l]
            else:
                r = mid - 1

        # we are on the right side
        else:
            # if on right side and target if lower than mid, we know we must look left from mid
            if target < nums[mid]:
                r = mid - 1
            # if target is higher than the rightmost value, we know we must look for our target left of mid
            elif target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
