class Solution:
    def __init__(self):
        self.visited = {}

    def climbStairs(self, n: int) -> int:
        if n in self.visited:
            return self.visited[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        res = self.climbStairs(n=n-1) + self.climbStairs(n=n-2)
        self.visited[n] = res
        return res
