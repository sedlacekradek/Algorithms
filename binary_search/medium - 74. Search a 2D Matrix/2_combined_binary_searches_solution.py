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
    # basically 2 binary searches, one to find the correct row and one to find the target in a row

    def get_row(matrix=matrix, target=target):
        # binary search to find the row
        l = 0
        r = len(matrix) - 1
        while l <= r:
            middle = (l+r) // 2
            # return True if the target is the highest or the lowest value of a given row
            # not really needed, but since we are checking the values anyway...
            if matrix[middle][0] == target or matrix[middle][len(matrix[middle])-1] == target:
                return True
            # if the target is between the lowest and the highest value of a row,
            # we found our row
            # matrix[middle][len(matrix[middle])-1] could also be written as matrix[middle][-1]
            if matrix[middle][0] <= target and matrix[middle][len(matrix[middle])-1] >= target:
                return middle
            # if the lowest value is too high, we need to look in one of the previous rows
            elif matrix[middle][0] > target:
                r = middle - 1
            # if the highest value is too low, we need to look in one of the following rows
            elif matrix[middle][len(matrix[middle])-1] < target:
                l = middle + 1
        # used -1 instead of False; we know that index can never be a negative value
        # if False was used, the func will bug out when middle = 0 because it will understand
        # 0 as a False boolean value
        return -1

    row = get_row()
    if row is True:
        return True
    # standard binary search
    if row != -1:
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            middle = (l+r) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                r = middle - 1
            elif matrix[row][middle] < target:
                l = middle + 1
        return False


print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
print(searchMatrix(matrix = [[1],[3]], target = 3))