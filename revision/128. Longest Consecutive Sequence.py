class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        unique = set()
        for n in nums:
            unique.add(n)

        res = 1
        counter = 1

        for n in unique:
            if n - 1 in unique:
                continue
            if n + 1 in unique:
                while n + counter in unique:
                    counter += 1
                res = max(res, counter)
                counter = 1

        return res