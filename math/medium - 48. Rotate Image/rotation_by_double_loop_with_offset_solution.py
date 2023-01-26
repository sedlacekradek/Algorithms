"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""


def rotate(matrix):
    left = 0
    right = len(matrix) - 1

    while left < right:
        # range of the reduced matrix -> right - left
        for i in range(right-left):
            # update top and bottom
            top, bottom = left, right
            # save the topleft
            temp_left = matrix[top][left+i]
            # move bottom left into top left
            matrix[top][left+i] = matrix[bottom-i][left]
            # move bottom right into bottom left
            matrix[bottom-i][left] = matrix[bottom][right-i]
            # move top right into bottom right
            matrix[bottom][right-i] = matrix[top+i][right]
            # move top left into top right
            matrix[top+i][right] = temp_left
        # reduce the matrix size once all outer values have been rotated
        left += 1
        right -= 1
    return matrix


print(rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))