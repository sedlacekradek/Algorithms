class Solution:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        visited = set()

        def count_area(r,c,grid,visited,rows,cols):
            around = [(1,0),(-1,0),(0,1),(0,-1)]
            area = 0
            from collections import deque
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                area += 1
                row, col = q.popleft()
                for vd, hd in around:
                    row2 = row + vd
                    col2 = col + hd
                    if row2 in range(rows) and col2 in range(cols) and grid[row2][col2] == 1 and (row2, col2) not in visited:
                        visited.add((row2,col2))
                        q.append((row2,col2))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = count_area(r,c,grid,visited,rows,cols)
                    res = max(res, area)
        return res

a = Solution()
print(a.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))