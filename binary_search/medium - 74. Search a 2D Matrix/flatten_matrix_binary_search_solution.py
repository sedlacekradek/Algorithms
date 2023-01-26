"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""
def searchMatrix(matrix, target):
    # flatter 2d matrix and solve with standard binary search
    import numpy as np
    matrix = np.array(matrix)
    matrix = list(matrix.flat)
    l = 0
    r = len(matrix) - 1

    while l <= r:
        middle = (l+r) // 2
        if matrix[middle] == target:
            return True
        if matrix[middle] > target:
            r = middle - 1
        if matrix[middle] < target:
            l = middle + 1
    return False


print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))