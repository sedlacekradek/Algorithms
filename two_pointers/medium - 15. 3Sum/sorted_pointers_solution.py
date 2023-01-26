"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

def threeSum(nums):
    nums = sorted(nums)
    result = []

    # convert problem into 2Sum with sorted array that can be solved with 2 pointers
    # iterate through array and solve a 2Sum problem for each element
    for i in range(0, len(nums)):
        # to avoid duplicate solutions/triplets
        # skip if nums[i] has already been serached for
        if i > 0 and nums[i] == nums[i-1]:
            continue
        i1 = i+1
        i2 = len(nums) - 1
        while i1 < i2:
            three_sum = nums[i] + nums[i1] + nums[i2]
            if three_sum < 0:
                i1 += 1
            elif three_sum > 0:
                i2 -= 1
            else:
                result.append([nums[i], nums[i1], nums[i2]])
                i1 += 1
                # to avoid duplicate solutions/triplets
                while nums[i1] == nums[i1-1] and i1 < i2:
                    i1 += 1
    return result






print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))
print(threeSum([-2,0,1,1,2,1]))
print(threeSum([-2,0,1,2,1,1]))
