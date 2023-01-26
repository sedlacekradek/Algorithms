"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

def setZeroes(matrix):

    def helper_col(col):
        for i in range(0, len(matrix)):
            if matrix[i][col] != 0:
                matrix[i][col] = "_"

    def helper_row(row):
        for i in range(0, len(matrix[0])):
            if matrix[row][i] != 0:
                matrix[row][i] = "_"

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if matrix[row][col] == 0:
                helper_col(col=col)
                helper_row(row=row)

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if matrix[row][col] == "_":
                matrix[row][col] = 0

    return matrix

print(setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

print(setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]]))
# [[1,0,1],[0,0,0],[1,0,1]]

print(setZeroes(matrix = [[0]]))
# [[0]]
