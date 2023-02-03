class Solution:

    def count_ones(self, grid, rows, cols):
        # count number of 1s in our grid
        counter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    counter += 1
        return counter

    def look_around(self, r, c, grid, grid2, rows, cols):
        # if 2 is found, look around to see if any 1s can be turned to 2
        around = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for vd, hd in around:
            row = r + vd
            col = c + hd
            # check if in bounds
            if row not in range(rows) or col not in range(cols):
                continue
            # update in our copy of grid to avoid recursion
            if grid[row][col] == 1:
                grid2[row][col] = 2

    def orangesRotting(self, grid: List[List[int]]) -> int:
        from copy import deepcopy
        grid2 = deepcopy(grid)
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        ones = self.count_ones(grid, rows, cols)

        while ones > 0:
            grid = deepcopy(grid2)
            res += 1
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 2:
                        self.look_around(r, c, grid, grid2, rows, cols)
            # if grid  did not change, we know solution not possible
            if grid == grid2:
                return -1
            # find new number of ones remaining
            ones = self.count_ones(grid2, rows, cols)
        return res