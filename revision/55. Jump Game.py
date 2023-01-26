def canJump(nums):
    goal_index = len(nums) - 1
    if len(nums) == 1:
        return True

    for i in range(len(nums) - 2, -1, -1):
        if (goal_index - i) <= nums[i]:
            goal_index = i

    return goal_index == 0