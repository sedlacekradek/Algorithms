def twoSum(nums, target):
    hash_map = {}

    for i in range(len(nums)):
        if nums[i] in hash_map:
            return [hash_map[nums[i]], i]
        to_get = target - nums[i]
        hash_map[to_get] = i