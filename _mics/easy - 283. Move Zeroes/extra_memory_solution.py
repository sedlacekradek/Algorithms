class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        to_pop = []
        for i in range(len(nums)):
            if nums[i] == 0:
                # store index of number we want to pop later
                to_pop.append(i)
                nums.append(0)
        # need to iterate in reverse order so that popping does not affect index of other numbers
        for n in to_pop[::-1]:
            nums.pop(n)