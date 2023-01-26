"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

def spiralOrder(matrix):
    left = top = 0
    right = len(matrix[0]) - 1
    bottom = len(matrix) - 1
    res = []


    while left < right and top < bottom:

        # from top-left to top-right
        for col in range(left, right):
            res.append(matrix[top][col])

        # from top-right to bottom-right
        for row in range(top, bottom):
            res.append(matrix[row][right])

        # from bottom-right to bottom-left
        for col in range(right, left, -1):
            res.append(matrix[bottom][col])

        # from bottom-left to top-left
        for row in range(bottom, top, -1):
            res.append(matrix[row][left])

        # adjust edges of the matrix
        left += 1
        right -= 1
        top += 1
        bottom -= 1

    # if not all matrix numbers included in res (which can happen for matrix of a certain size)
    # go through these lines from left to right and add them to result
    if len(res) < len(matrix) * len(matrix[0]):
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                res.append(matrix[row][col])

    return res

print(spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# [1,2,3,4,8,12,11,10,9,5,6,7]
print(spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
# [1,2,3,6,9,8,7,4,5]
print(spiralOrder(matrix = [[6,9,7]]))
# [6,9,7]
print(spiralOrder(matrix = [[3],[2]]))
# [[3,2]]
