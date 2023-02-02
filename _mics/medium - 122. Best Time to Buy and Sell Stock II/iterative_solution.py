class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float("inf")
        profit = 0

        for n in prices:
            if n > min_buy:
                profit += n - min_buy
                min_buy = n
            if n < min_buy:
                min_buy = n

        return profit
