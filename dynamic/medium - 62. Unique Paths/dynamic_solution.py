class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        backtracks from the GOAL and calculates possible movements for each field by summing
        previous field in the same row and the field below in the same column:

        [10, 6, 3, 1]
        [4, 3, 2, 1]
        [1, 1, 1, 1]

        result is 10
        """

        # initiate first row with all 1s
        row = [1 for _ in range(n)]
        # generate numbers of all other rows; m-1 because we already initiated the first row
        for i in range(m - 1):
            # initiate a new line with all 1x
            new_row = [1 for _ in range(n)]
            # iterate through the line from the back
            for j in range(n - 2, -1, -1):
                # sum of previous field + field below
                new_row[j] = new_row[j + 1] + row[j]
            # update the row below
            row = new_row
        # the very first field will store the result
        return row[0]
