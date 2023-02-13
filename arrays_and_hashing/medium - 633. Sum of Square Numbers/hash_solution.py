class Solution:
    def judgeSquareSum(self, n: int) -> bool:
        if n == 0:
            return True

        squares = set()
        for f in range(1, int(n ** 0.5) + 1):
            squares.add(f ** 2)

        for s in squares:
            if n - s in squares or s == n:
                return True

        return False