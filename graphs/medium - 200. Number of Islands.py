class Solution:
    def update_visited(self, row, col, visited, grid):
        around = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        from collections import deque
        q = deque()
        q.append((row, col))
        visited.add((row, col))
        while q:
            current = q.popleft()
            for r, c in around:
                if current[0] + r < len(grid) and \
                        current[0] + r >= 0 and \
                        current[1] + c < len(grid[0]) and \
                        current[1] + c >= 0 and \
                        grid[current[0] + r][current[1] + c] == "1" and \
                        (current[0] + r,current[1] + c) not in visited:
                    visited.add((current[0] + r, current[1] + c))
                    q.append((current[0] + r, current[1] + c))

    def numIslands(self, grid):
        if not grid:
            return 0

        islands = 0
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and ((row, col) not in visited):
                    islands += 1
                    self.update_visited(row, col, visited, grid)
        return islands


a = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(a.numIslands(grid))