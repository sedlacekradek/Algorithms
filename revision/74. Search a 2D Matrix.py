class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = 0

        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] > target:
                high = mid - 1
            else:
                row = mid
                low = mid + 1

        if len(matrix[0]) < 2:
            if matrix[row][0] == target:
                return True
            else:
                return False
        else:
            low = 0
            high = len(matrix[0]) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[row][mid] == target:
                    return True
                if matrix[row][mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

        return False