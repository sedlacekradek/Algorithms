def numberOfArithmeticSlices(nums):
    count = 0
    result = 0

    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            count += 1
            result += count
        else:
            count = 0

    return result