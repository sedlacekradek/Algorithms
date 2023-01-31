class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        counter = 1
        majority = nums[0]

        for n in nums[1:]:
            if counter == 0:
                majority = n
                counter += 1
            elif n == majority:
                counter += 1
            elif n != majority:
                counter -= 1

        return majority