def jump(nums):
    l = 0
    r = 0
    res = 0
    jump = 0

    if len(nums) == 1:
        return 0

    while r < len(nums) - 1: # do not forget -1
        for i in range(l, r+1):
            jump = max(jump, nums[i] + i)
        res += 1
        l = r
        r = jump
    return res


print(jump([1,1,1,99,0,0,0,0,0]))
print(jump([0]))
print(jump([1]))
print(jump([1,1]))
print(jump([99,0,0,0,0,0,0,0,0]))
print(jump([2,0,99,0,0,0,0,0,0]))
