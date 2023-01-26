def twoSum(nums, target):

    seen = {}

    for i, value in enumerate(nums):
        remainder = target - value

        if remainder in seen:
            return seen[remainder], i

        else:
            seen[value] = i

# print(twoSum([2,7,11,15], 26))
print(twoSum([-1,-2,-3,-4,-5], -8))