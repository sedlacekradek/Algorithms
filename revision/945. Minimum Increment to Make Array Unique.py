def minIncrementForUnique(self, nums: List[int]) -> int:
    nums.sort()
    min_val = float("-inf")
    res = 0

    for n in nums:
        if n > min_val:
            min_val = n
        else:
            res += (min_val - n) + 1
            min_val += 1

    return res
