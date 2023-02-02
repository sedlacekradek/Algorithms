class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        mover = 0

        while mover <= right:
            if nums[mover] == 0:
                nums[left], nums[mover] = nums[mover], nums[left]
                left += 1
                mover += 1
            elif nums[mover] == 1:
                mover += 1
            else:
                nums[right], nums[mover] = nums[mover], nums[right]
                right -= 1
                # important NOT mover += 1
                # the number moved from right could be a 0 and we may need to move it left before continuing with our loop
