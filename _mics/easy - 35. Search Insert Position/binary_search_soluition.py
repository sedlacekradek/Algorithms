

def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1
    diff = float("inf")

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            high = mid - 1
            if nums[mid] - target < diff:
                diff = nums[mid] - target
                return_num = mid
        else:
            low = mid + 1
            if target - nums[mid] < diff:
                diff = target - nums[mid]
                return_num = mid + 1

    return return_num

print(searchInsert([1,3], 2))
print(searchInsert([1,3,5,6], 2))