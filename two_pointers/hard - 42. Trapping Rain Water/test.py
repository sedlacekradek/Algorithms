"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""


def trap(height):
    # solution: iterate through array and calculate how much water we can keep at each separate space
    # we need to find the highest value left of the field and right of the field
    # then pick the lower of these two values (x) and calc: field_value - x = water_at_space
    # if this gives < 0 value, convert to 0
    # return the sum of all these values

    left_max_list = [[] for _ in range(0, len(height))]
    right_max_list = [[] for _ in range(0, len(height))]

    result = 0
    left_max = 0
    right_max = 0

    # create array of left_maxes
    for i in range(0, len(height)):
        left_max_list[i] = left_max
        if height[i] > left_max:
            left_max = height[i]

    # create array of right_maxes
    for i in reversed(range(0, len(height))):
        right_max_list[i] = right_max
        if height[i] > right_max:
            right_max = height[i]

    # use the calculation to get how much water each field holds and add it to the final result
    for i in range(0, len(height)):
        water = min(left_max_list[i], right_max_list[i]) - height[i]
        # convert negatives to 0
        if water < 0:
            water = 0
        result += water

    return result


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))
print(trap([4,2,3]))