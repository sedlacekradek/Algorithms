"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height =
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

def maxArea(height):
    # O(n) solution
    i1 = 0
    i2 = len(height) - 1
    result = 0

    while i1 < i2:
        # calc the area -> length x height of the lower wall
        area = min(height[i1], height[i2]) * (i2-i1)
        # update result if higher result found
        if area > result:
            result = area
        # unlike brute force where we check all possible combinations
        # here we only change the index of the lower wall
        # this can potentially bring us higher area result
        if height[i1] <= height[i2]:
            i1 += 1
        elif height[i2] < height[i1]:
            i2 -= 1
    return result

print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1,1]))